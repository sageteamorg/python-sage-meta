import logging
from typing import List, Optional

import requests


logger = logging.getLogger(__name__)


class InstagramProductTagging:
    """
    Class to handle Instagram product tagging via the Graph API.
    """

    def __init__(self, access_token: str) -> None:
        """
        Initialize the InstagramProductTagging instance.

        Args:
            access_token (str): Facebook access token.
        """
        self.access_token = access_token
        self.graph_url = "https://graph.facebook.com/v11.0"

    def create_tagged_container(
        self,
        ig_user_id: str,
        media_type: str,
        media_url: str,
        product_tags: list,
        caption: Optional[str] = None,
        user_tags: Optional[List[dict]] = None,
        thumb_offset: int = 0,
        location_id: Optional[str] = None,
        share_to_feed: bool = False,
    ) -> dict:
        """
        Create a tagged media container.

        Args:
            ig_user_id (str): Instagram user ID.
            media_type (str): Type of media (IMAGE, VIDEO, REELS).
            media_url (str): URL of the media to be uploaded.
            product_tags (list): List of product tags.
            caption (str, optional): Caption for the media. Defaults to None.
            user_tags (list, optional): List of user tags. Defaults to None.
            thumb_offset (int, optional): Thumbnail offset for video. Defaults to 0.
            location_id (str, optional): Location ID. Defaults to None.
            share_to_feed (bool, optional): Whether to share to feed for REELS. Defaults to False.

        Returns:
            dict: Response from the API.
        """
        url = f"{self.graph_url}/{ig_user_id}/media"
        params = {
            "media_type": media_type,
            "access_token": self.access_token,
            "product_tags": product_tags,
        }

        if media_type == "IMAGE":
            params["image_url"] = media_url
            if user_tags:
                params["user_tags"] = user_tags
        elif media_type in ["VIDEO", "REELS"]:
            params["video_url"] = media_url
            params["thumb_offset"] = thumb_offset

        if caption:
            params["caption"] = caption

        if location_id:
            params["location_id"] = location_id

        if media_type == "REELS":
            params["share_to_feed"] = share_to_feed

        try:
            response = requests.post(url, data=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error("Error creating tagged container: %s", e)
            return {"error": str(e)}

    def publish_media(self, ig_user_id: str, creation_id: str) -> dict:
        """
        Publish a media container.

        Args:
            ig_user_id (str): Instagram user ID.
            creation_id (str): Creation ID of the media container.

        Returns:
            dict: Response from the API.
        """
        url = f"{self.graph_url}/{ig_user_id}/media_publish"
        params = {"creation_id": creation_id, "access_token": self.access_token}
        try:
            response = requests.post(url, data=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error("Error publishing media: %s", e)
            return {"error": str(e)}

    def get_product_tags(self, media_id: str) -> dict:
        """
        Get product tags of a media.

        Args:
            media_id (str): Media ID.

        Returns:
            dict: Product tags of the media.
        """
        url = f"{self.graph_url}/{media_id}?fields=product_tags"
        params = {"access_token": self.access_token}
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error("Error getting product tags: %s", e)
            return {"error": str(e)}

    def delete_product_tags(self, media_id: str) -> dict:
        """
        Delete product tags of a media.

        Args:
            media_id (str): Media ID.

        Returns:
            dict: Response from the API.
        """
        url = f"{self.graph_url}/{media_id}/product_tags"
        params = {"access_token": self.access_token}
        try:
            response = requests.delete(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error("Error deleting product tags: %s", e)
            return {"error": str(e)}

    def update_product_tags(self, media_id: str, product_tags: list) -> dict:
        """
        Update product tags of a media.

        Args:
            media_id (str): Media ID.
            product_tags (list): List of new product tags.

        Returns:
            dict: Response from the API.
        """
        url = f"{self.graph_url}/{media_id}/product_tags"
        params = {"product_tags": product_tags, "access_token": self.access_token}
        try:
            response = requests.post(url, data=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error("Error updating product tags: %s", e)
            return {"error": str(e)}

    def get_catalogs(self, ig_user_id: str) -> dict:
        """
        Get available catalogs for an Instagram user.

        Args:
            ig_user_id (str): Instagram user ID.

        Returns:
            dict: Available catalogs.
        """
        url = f"{self.graph_url}/{ig_user_id}/available_catalogs"
        params = {"access_token": self.access_token}
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error("Error getting catalogs: %s", e)
            return {"error": str(e)}

    def get_eligible_products(
        self, ig_user_id: str, catalog_id: str, query: Optional[str] = None
    ) -> dict:
        """
        Get eligible products from a catalog.

        Args:
            ig_user_id (str): Instagram user ID.
            catalog_id (str): Catalog ID.
            query (str, optional): Search query. Defaults to None.

        Returns:
            dict: Eligible products.
        """
        url = f"{self.graph_url}/{ig_user_id}/catalog_product_search"
        params = {"catalog_id": catalog_id, "access_token": self.access_token}
        if query:
            params["q"] = query
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error("Error getting eligible products: %s", e)
            return {"error": str(e)}

    def create_catalog(self, business_id: str, catalog_name: str) -> dict:
        """
        Create a new product catalog.

        Args:
            business_id (str): Business ID.
            catalog_name (str): Name of the new catalog.

        Returns:
            dict: Response from the API.
        """
        url = f"{self.graph_url}/{business_id}/owned_product_catalogs"
        params = {"name": catalog_name, "access_token": self.access_token}
        try:
            response = requests.post(url, data=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error("Error creating catalog: %s", e)
            return {"error": str(e)}
