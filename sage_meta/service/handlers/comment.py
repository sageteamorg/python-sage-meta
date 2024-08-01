import logging
from typing import List, Optional

import requests

from sage_meta.models import Comment, CommentMention, PostMention, ReplyMention

logger = logging.getLogger(__name__)

class CommentHandler:
    def __init__(self, client:"FacebookClient"):
        self.client = client

    def get_instagram_comments(self, media_id: str) -> List[Comment]:
        """
        Fetch comments for a given Instagram media ID.

        Args:
            media_id (str): Instagram media ID.

        Returns:
            List[Comment]: List of comments.
        """
        url = f"{self.client.graph_url}/{media_id}/comments"
        params = {
            "fields": "id,text,username,like_count,timestamp,user",
            "access_token": self.client.access_token,
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            comments_data = response.json()

            comments_list = [
                self._parse_comment_item(comment)
                for comment in comments_data.get("data", [])
            ]
            print(f"Retrieved {len(comments_list)} comments.")
            return comments_list
        except requests.HTTPError as http_err:
            error_message = (
                response.json().get("error", {}).get("message", "Unknown error")
            )
            logger.error(
                f"HTTP error occurred: {http_err}. Error message: {error_message}"
            )
        except requests.RequestException as req_err:
            logger.error(f"Request exception occurred: {req_err}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
        return []

    def _parse_comment_item(self, comment: dict) -> Comment:
        """
        Parse a comment item from the API response.

        Args:
            comment (dict): Comment data.

        Returns:
            Comment: Parsed comment object.
        """
        additional_data = {
            k: v
            for k, v in comment.items()
            if k not in {"id", "text", "username", "like_count", "timestamp", "user"}
        }
        return Comment(
            id=comment["id"],
            text=comment.get("text"),
            username=comment.get("username"),
            like_count=comment.get("like_count"),
            timestamp=comment.get("timestamp"),
            additional_data=additional_data,
        )

    def get_post_mentions(self, insta_id: str, media_id: str) -> Optional[PostMention]:
        """
        Fetch data about media posts where the IG user is mentioned in the caption.

        Args:
            insta (str): Instagram account ID.
            media_id (str): Media ID where the user is mentioned.

        Returns:
            Optional[PostMention]: Post mention details or None.
        """
        url = f"{self.client.graph_url}/{insta_id}"
        params = {
            "fields": f"mentioned_media.media_id({media_id}){{id,media_type,media_url,caption,comments_count,like_count,timestamp,username,owner}}",
            "access_token": self.client.access_token,
        }

        logger.debug(f"Request URL: {url}")
        logger.debug(f"Request parameters: {params}")

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json().get("mentioned_media", {})
            if data:
                return PostMention(
                    id=data.get("id"),
                    media_type=data.get("media_type"),
                    media_url=data.get("media_url"),
                    caption=data.get("caption", ""),
                    comments_count=data.get("comments_count", 0),
                    like_count=data.get("like_count", 0),
                    timestamp=data.get("timestamp", ""),
                    username=data.get("username", ""),
                    owner=data.get("owner", ""),
                    additional_data={},
                )
            return None
        except requests.HTTPError as http_err:
            error_data = response.json().get("error", {})
            if error_data.get("code") == 10:
                logger.error("User is not mentioned in the caption.")
            else:
                logger.error(
                    f"HTTP error occurred: {http_err}. Error message: {error_data.get('message')}"
                )
            return None
        except requests.RequestException as req_err:
            logger.error(f"Request exception occurred: {req_err}")
            return None

    def get_comment_mentions(
        self, insta_id: str, comment_id: str
    ) -> Optional[CommentMention]:
        """
        Get data about comments in which the account has been mentioned.

        Args:
            comment_id (str): Comment ID where the account is mentioned.

        Returns:
            Optional[CommentMention]: Comment mention details or None.
        """
        url = f"{self.client.graph_url}/{insta_id}"
        params = {
            "fields": f"mentioned_comment.comment_id({comment_id}){{timestamp,like_count,text,username,id}}",
            "access_token": self.client.access_token,
        }

        logger.debug(f"Request URL: {url}")
        logger.debug(f"Request parameters: {params}")

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json().get("mentioned_comment", {})
            if data:
                return CommentMention(
                    id=data.get("id"),
                    text=data.get("text", ""),
                    like_count=data.get("like_count", 0),
                    timestamp=data.get("timestamp", ""),
                    username=data.get("username", ""),
                    additional_data={},
                )
            return None
        except requests.HTTPError as http_err:
            error_data = response.json().get("error", {})
            if error_data.get("code") == 10:
                logger.error("User is not mentioned in the comment.")
            else:
                logger.error(
                    f"HTTP error occurred: {http_err}. Error message: {error_data.get('message')}"
                )
            return None
        except requests.RequestException as req_err:
            logger.error(f"Request exception occurred: {req_err}")
            return None

    def reply_to_mention(
        self, insta_id: str, comment_id: Optional[str], message: str, media_id: str
    ) -> Optional[ReplyMention]:
        """
        Reply to a comment or media object caption that the account has been mentioned in.

        Args:
            insta (str): Instagram account ID.
            comment_id (Optional[str]): Comment ID (if replying to a comment).
            message (str): Reply message.
            media_id (str): Media ID where the comment is.

        Returns:
            Optional[ReplyMention]: Reply mention details or None.
        """
        url = f"{self.client.graph_url}/{insta_id}/mentions"
        params = {
            "media_id": media_id,
            "message": message,
            "access_token": self.client.access_token,
        }
        if comment_id:
            params["comment_id"] = comment_id

        logger.debug(f"Request URL: {url}")
        logger.debug(f"Request parameters: {params}")

        try:
            response = requests.post(url, data=params)
            response.raise_for_status()
            data = response.json()
            logger.debug(f"Reply to mention response: {data}")
            return ReplyMention(
                id=data.get("id"),
                message=message,
                timestamp=data.get("timestamp", ""),
                additional_data={},
            )
        except requests.RequestException as e:
            logger.error(f"Error replying to mention: {e}")
            logger.debug(f"Response content: {e.response.content}")
            return None
