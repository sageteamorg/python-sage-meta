import logging
from typing import List

import facebook

from sage_meta.models import Story

logger = logging.getLogger(__name__)


class StoryHandler:
    def __init__(self, client: "FacebookClient"):
        self.client = client

    def get_instagram_stories(self, insta_id: str) -> List[Story]:
        """
        Fetch Instagram stories for a given Instagram account ID.

        Args:
            insta_id (str): Instagram account ID.

        Returns:
            List[Story]: List of Instagram stories.
        """
        try:
            stories_data = self.client.graph.get_connections(
                insta_id, "stories", fields="id,media_type,media_url,timestamp"
            )
            stories_list = [
                self._parse_story_item(story) for story in stories_data["data"]
            ]
            logger.info("Retrieved %d stories.", len(stories_list))
            return stories_list
        except facebook.GraphAPIError as e:
            logger.error("Error fetching Instagram stories: %s", e)
            return []

    def _parse_story_item(self, story: dict) -> Story:
        additional_data = {
            k: v
            for k, v in story.items()
            if k not in {"id", "media_type", "media_url", "timestamp"}
        }
        return Story(
            id=story["id"],
            media_type=story.get("media_type"),
            media_url=story.get("media_url"),
            timestamp=story.get("timestamp"),
            additional_data=additional_data,
        )
