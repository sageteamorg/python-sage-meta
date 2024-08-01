import logging
import requests
from typing import List, Optional
import facebook

logger = logging.getLogger(__name__)

class ContentPublishing:
    """
    Class to handle content publishing on Instagram via the Graph API.
    """

    def __init__(self, client) -> None:
        """
        Initialize the ContentPublishing instance.

        Args:
            client (FacebookClient): The Facebook client instance.
        """
        self.client = client

    def publish_photo(self, image_url: str, caption: str) -> dict:
        """
        Publish a photo to Instagram.

        Args:
            image_url (str): URL of the image to be published.
            caption (str): Caption for the photo.

        Returns:
            dict: Response from the API.
        """
        logger.debug("Publishing photo to Instagram.")
        try:
            response = self.client.graph.put_object(
                parent_object=self.client.insta_business,
                connection_name="media",
                image_url=image_url,
                caption=caption,
            )
            creation_id = response["id"]
            publish_response = self.client.graph.put_object(
                parent_object=self.client.insta_business,
                connection_name="media_publish",
                creation_id=creation_id,
            )
            return publish_response
        except facebook.GraphAPIError as e:
            logger.error("Error publishing photo: %s", e)
            return {"error": str(e)}

    def publish_video(self, video_url: str, caption: str) -> dict:
        """
        Publish a video to Instagram.

        Args:
            video_url (str): URL of the video to be published.
            caption (str): Caption for the video.

        Returns:
            dict: Response from the API.
        """
        media_container_id = self.upload_video(video_url, caption)
        if not media_container_id:
            return {"error": "Upload failed"}

        try:
            publish_response = requests.post(
                f"{self.client.graph_url}/{self.client.insta_business}/media_publish",
                data={
                    "creation_id": media_container_id,
                    "access_token": self.client.access_token,
                },
                timeout=10
            )
            publish_data = publish_response.json()
            logger.info("Video published. Media ID: %s", publish_data.get('id'))
            return publish_data
        except requests.RequestException as e:
            logger.error("Error publishing video: %s", e)
            return {"error": str(e)}

    def upload_video(self, video_url: str, caption: str) -> Optional[str]:
        """
        Upload a video to Instagram.

        Args:
            video_url (str): URL of the video to be uploaded.
            caption (str): Caption for the video.

        Returns:
            Optional[str]: Media container ID of the uploaded video or None if failed.
        """
        logger.debug("Uploading video to Instagram.")
        try:
            create_response = requests.post(
                f"{self.client.graph_url}/{self.client.insta_business}/media",
                data={
                    "media_type": "REELS",
                    "video_url": video_url,
                    "caption": caption,
                    "access_token": self.client.access_token,
                },
                timeout=10
            )
            create_response.raise_for_status()
            create_data = create_response.json()
            media_container_id = create_data["id"]
            logger.info("Video uploaded. Media container ID: %s", media_container_id)
            return media_container_id
        except requests.RequestException as e:
            logger.error("Error uploading video: %s", e)
            return None

    def publish_carousel(self, media_urls: List[str], caption: str) -> dict:
        """
        Publish a carousel to Instagram.

        Args:
            media_urls (List[str]): List of URLs of the media to be included in the carousel.
            caption (str): Caption for the carousel.

        Returns:
            dict: Response from the API.
        """
        logger.debug("Publishing carousel to Instagram.")
        try:
            media_ids = []
            for url in media_urls:
                response = self.client.graph.put_object(
                    parent_object=self.client.insta_business,
                    connection_name="media",
                    image_url=url,
                    is_carousel_item=True,
                )
                media_ids.append(response["id"])

            carousel_response = self.client.graph.put_object(
                parent_object=self.client.insta_business,
                connection_name="media",
                media_type="CAROUSEL",
                children=",".join(media_ids),
                caption=caption,
            )
            creation_id = carousel_response["id"]

            publish_response = self.client.graph.put_object(
                parent_object=self.client.insta_business,
                connection_name="media_publish",
                creation_id=creation_id,
            )
            return publish_response
        except facebook.GraphAPIError as e:
            logger.error("Error publishing carousel: %s", e)
            return {"error": str(e)}

    def get_media_status(self, media_id: str) -> dict:
        """
        Get the status of a media item.

        Args:
            media_id (str): Media ID.

        Returns:
            dict: Status of the media item.
        """
        logger.debug("Getting media status.")
        try:
            status_response = requests.get(
                f"{self.client.graph_url}/{media_id}",
                params={
                    "fields": "status_code,status",
                    "access_token": self.client.access_token,
                },
                timeout=10
            )
            status_response.raise_for_status()
            status_data = status_response.json()
            return status_data
        except requests.RequestException as e:
            logger.error("Error getting media status: %s", e)
            return {"error": str(e)}

    def put_comment(self, post_id: str, message: str) -> dict:
        """
        Post a comment to a post.

        Args:
            post_id (str): Post ID.
            message (str): Comment message.

        Returns:
            dict: Response from the API.
        """
        logger.debug("Posting a comment to the post.")
        try:
            comment = self.client.graph.put_comment(post_id, message=message)
            logger.info("Comment posted: %s", comment)
            return comment
        except facebook.GraphAPIError as e:
            logger.error("Error posting comment: %s", e)
            return {"error": str(e)}

    def reply_to_comment(self, comment_id: str, message: str) -> dict:
        """
        Reply to a comment.

        Args:
            comment_id (str): Comment ID.
            message (str): Reply message.

        Returns:
            dict: Response from the API.
        """
        logger.debug("Replying to comment.")
        try:
            response = requests.post(
                f"{self.client.graph_url}/{comment_id}/replies",
                data={"message": message, "access_token": self.client.access_token},
                timeout=10
            )
            response.raise_for_status()
            logger.info("Reply posted: %s", response.json())
            return response.json()
        except requests.RequestException as e:
            logger.error("Error replying to comment: %s", e)
            return {"error": str(e)}

    def publish_story(self, image_url: str) -> dict:
        """
        Publish a story to Instagram.

        Args:
            image_url (str): URL of the image to be published as a story.

        Returns:
            dict: Response from the API.
        """
        logger.debug("Publishing story to Instagram.")
        try:
            response = requests.post(
                f"{self.client.graph_url}/{self.client.insta_business}/media",
                data={
                    "media_type": "STORIES",
                    "image_url": image_url,
                    "access_token": self.client.access_token,
                },
                timeout=10
            )
            response.raise_for_status()
            response_data = response.json()
            creation_id = response_data["id"]

            publish_response = requests.post(
                f"{self.client.graph_url}/{self.client.insta_business}/media_publish",
                data={"creation_id": creation_id, "access_token": self.client.access_token},
                timeout=10
            )
            publish_response.raise_for_status()
            logger.info("Story published: %s", publish_response.json())
            return publish_response.json()
        except requests.RequestException as e:
            logger.error("Error publishing story: %s", e)
            return {"error": str(e)}
