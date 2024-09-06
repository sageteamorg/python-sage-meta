import logging
from typing import List, Optional

import facebook
import requests

from sage_meta.models import Category, FacebookPageData, InstagramAccount

logger = logging.getLogger(__name__)


class AccountHandler:
    def __init__(self, client: "FacebookClient"):
        self.client = client

    def get_accounts(self) -> List[FacebookPageData]:
        """
        Fetch the user's Facebook pages.

        Returns:
            List[FacebookPageData]: List of user's Facebook pages.
        """
        if self.client.user is None:
            logger.error("Client user is None")
            return []

        logger.debug("Fetching accounts for user ID: %s", self.client.user.id)
        try:
            accounts_data = self.client.graph.get_connections(
                self.client.user.id, "accounts"
            )
            accounts = accounts_data.get("data", [])

            self.client.user.pages = [
                self._parse_page_data(account) for account in accounts
            ]
            return self.client.user.pages
        except facebook.GraphAPIError as e:
            logger.error("Error fetching accounts: %s", e)
            return []

    def _parse_page_data(self, account: dict) -> FacebookPageData:
        category_list = [
            Category(cat["id"], cat["name"]) for cat in account.get("category_list", [])
        ]
        additional_data = {
            k: v
            for k, v in account.items()
            if k
            not in {"id", "name", "category", "category_list", "tasks", "access_token"}
        }
        page = FacebookPageData(
            id=account["id"],
            name=account["name"],
            category=account["category"],
            category_list=category_list,
            tasks=account["tasks"],
            access_token=account["access_token"],
            additional_data=additional_data,
        )
        page.instagram_business_account = self.get_instagram_business_account(page)
        return page

    def get_instagram_business_account(
        self, page: FacebookPageData
    ) -> Optional[InstagramAccount]:
        """
        Fetch the Instagram business account linked to a Facebook page.

        Args:
            page (FacebookPageData): The Facebook page data.

        Returns:
            Optional[InstagramAccount]: Instagram business account data or None.
        """
        logger.debug(
            "Fetching Instagram business account for page ID: %s, Page Name: %s",
            page.id,
            page.name,
        )
        try:
            data = self.client.graph.get_object(
                page.id, fields="instagram_business_account"
            )
            if "instagram_business_account" in data:
                insta_id = data["instagram_business_account"]["id"]
                self.client.insta_business = insta_id
                logger.debug("Instagram business account ID: %s", insta_id)
                account_data = self.client.graph.get_object(
                    insta_id,
                    fields=(
                        "id,username,follows_count,followers_count,media_count,"
                        "profile_picture_url,website,biography"
                    ),
                )
                media = self.client.media_handler.get_instagram_media(insta_id)
                insights = self.client.media_handler.get_instagram_insights(insta_id)
                stories = self.client.story_handler.get_instagram_stories(insta_id)
                comments = []
                for post in media:
                    comments.extend(
                        self.client.comment_handler.get_instagram_comments(post.id)
                    )
                additional_data = {
                    k: v
                    for k, v in account_data.items()
                    if k
                    not in {
                        "id",
                        "username",
                        "follows_count",
                        "followers_count",
                        "media_count",
                        "profile_picture_url",
                        "website",
                        "biography",
                    }
                }
                account = InstagramAccount(
                    id=account_data["id"],
                    username=account_data["username"],
                    follows_count=account_data["follows_count"],
                    followers_count=account_data["followers_count"],
                    media_count=account_data["media_count"],
                    profile_picture_url=account_data.get("profile_picture_url"),
                    website=account_data.get("website"),
                    biography=account_data.get("biography"),
                    media=media,
                    insights=insights,
                    stories=stories,
                    additional_data=additional_data,
                )
                logger.info("Retrieved Instagram account data: %s", account)
                return account
            logger.warning(
                "No Instagram business account linked to page ID: %s", page.id
            )
            return None
        except facebook.GraphAPIError as e:
            logger.error("Error fetching Instagram business account: %s", e)
            return None

    def get_account_settings(self) -> dict:
        """
        Get the settings of an Instagram account.

        Returns:
            dict: Instagram account settings.
        """
        if not self.client.insta_business:
            logger.error("No Instagram business account ID available")
            return {"error": "No Instagram business account ID available"}

        try:
            response = self._make_request(
                f"{self.client.graph_url}/{self.client.insta_business}",
                params={
                    "access_token": self.client.access_token,
                    "fields": "biography,website",
                },
            )
            return response.json()
        except requests.RequestException as e:
            logger.error("Error getting account settings: %s", e)
            return {"error": str(e)}

    def _make_request(self, url: str, params: dict) -> requests.Response:
        """
        Make a GET request with the given URL and parameters, including a timeout.

        Args:
            url (str): The URL for the request.
            params (dict): The parameters for the request.

        Returns:
            requests.Response: The response from the GET request.

        Raises:
            requests.RequestException: If the request fails.
        """
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logger.error("Request failed: %s", e)
            raise
