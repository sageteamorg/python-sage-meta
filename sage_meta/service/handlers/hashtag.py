import logging
from typing import List, Optional, Dict

import requests


logger = logging.getLogger(__name__)

class HashtagHandler:
    def __init__(self, client: "FacebookClient"):
        self.client = client

    def search_hashtag(self, insta_id: str, query: str) -> Optional[str]:
        """
        Search for a hashtag.

        Args:
            insta_id (str): Instagram account ID.
            query (str): Hashtag to search for.

        Returns:
            Optional[str]: Hashtag ID or None.
        """
        url = f"{self.client.graph_url}/ig_hashtag_search"
        params = {
            "user_id": insta_id,
            "q": query,
            "access_token": self.client.access_token,
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            logger.debug(f"Searched hashtag response: {data}")
            if "data" in data:
                return data["data"][0]["id"]
            return None
        except requests.RequestException as e:
            logger.error(f"Error searching hashtag: {e}")
            return None

    def get_hashtag_info(self, hashtag_id: str) -> Dict:
        """
        Get information about a hashtag.

        Args:
            hashtag_id (str): Hashtag ID.

        Returns:
            dict: Hashtag information.
        """
        url = f"{self.client.graph_url}/{hashtag_id}"
        params = {"access_token": self.client.access_token}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching hashtag info: {e}")
            return {}

    def get_recent_media(self, hashtag_id: str, insta_id: str) -> Dict:
        """
        Get recent media for a given hashtag.

        Args:
            hashtag_id (str): Hashtag ID.
            insta_id (str): Instagram account ID.

        Returns:
            dict: Recent media data.
        """
        url = f"{self.client.graph_url}/{hashtag_id}/recent_media"
        params = {
            "user_id": insta_id,
            "fields": "id,caption,media_type,media_url,permalink",
            "access_token": self.client.access_token,
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching recent media: {e}")
            return {}

    def get_top_media(self, hashtag_id: str, insta_id: str) -> List[Dict]:
        """
        Get top media for a given hashtag.

        Args:
            hashtag_id (str): Hashtag ID.
            insta_id (str): Instagram account ID.

        Returns:
            List[dict]: List of top media data.
        """
        url = f"{self.client.graph_url}/{hashtag_id}/top_media"
        params = {
            "user_id": insta_id,
            "fields": "id,media_type,comments_count,like_count",
            "access_token": self.client.access_token,
            "limit": 10,
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching top media: {e}")
            return []
