import logging

from sage_meta.utils import get_request

logger = logging.getLogger(__name__)


class CopyrightManager:
    """
    Class to manage copyright information via the Graph API.
    """

    def __init__(self, access_token: str) -> None:
        """
        Initialize the CopyrightManager instance.

        Args:
            access_token (str): Facebook access token.
        """
        self.access_token = access_token
        self.graph_url = "https://graph.facebook.com/v11.0"

    def check_copyright_status_unpublished(self, container_id: str) -> dict:
        """
        Check the copyright status of an uploaded, but not yet published, video.

        Args:
            container_id (str): Instagram container ID.

        Returns:
            dict: Response from the API.
        """
        url = f"{self.graph_url}/{container_id}"
        params = {
            "fields": "copyright_check_status",
            "access_token": self.access_token,
        }
        return get_request(url, params)

    def check_copyright_status_published(self, media_id: str) -> dict:
        """
        Check the copyright status of a published video.

        Args:
            media_id (str): Instagram media ID.

        Returns:
            dict: Response from the API.
        """
        url = f"{self.graph_url}/{media_id}"
        params = {
            "fields": "copyright_check_information",
            "access_token": self.access_token,
        }
        return get_request(url, params)
