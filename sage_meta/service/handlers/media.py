import logging
from typing import List

import facebook

from sage_meta.models import Insight, Media

logger = logging.getLogger(__name__)


class MediaHandler:
    def __init__(self, client:"FacebookClient"):
        self.client = client

    def get_instagram_media(self, insta_id: str) -> List[Media]:
        """
        Fetch Instagram media for a given Instagram account ID.

        Args:
            insta_id (str): Instagram account ID.

        Returns:
            List[Media]: List of Instagram media items.
        """
        try:
            media_data = self.client.graph.get_connections(
                insta_id,
                "media",
                fields="id,caption,media_type,media_url,timestamp,like_count,comments_count",
            )
            media_list = [self._parse_media_item(media) for media in media_data["data"]]
            logger.info(f"Retrieved {len(media_list)} media items.")
            return media_list
        except facebook.GraphAPIError as e:
            logger.error(f"Error fetching Instagram media: {e}")
            return []

    def _parse_media_item(self, media: dict) -> Media:
        media_urls = []
        if media.get("media_type") == "CAROUSEL_ALBUM":
            children_data = self.client.graph.get_connections(
                media["id"], "children", fields="media_url"
            )
            media_urls = [child["media_url"] for child in children_data["data"]]
        else:
            media_urls.append(media.get("media_url"))

        additional_data = {
            k: v
            for k, v in media.items()
            if k
            not in {
                "id",
                "caption",
                "media_type",
                "media_url",
                "timestamp",
                "like_count",
                "comments_count",
            }
        }
        return Media(
            id=media["id"],
            caption=media.get("caption"),
            media_type=media.get("media_type"),
            media_url=media_urls,
            timestamp=media.get("timestamp"),
            like_count=media.get("like_count"),
            comments_count=media.get("comments_count"),
            additional_data=additional_data,
        )

    def get_instagram_insights(self, insta_id: str) -> List[Insight]:
        """
        Fetch insights for a given Instagram account ID.

        Args:
            insta_id (str): Instagram account ID.

        Returns:
            List[Insight]: List of insights.
        """
        metrics_periods = {
            "impressions": ["day", "lifetime"],
            "reach": ["day", "lifetime"],
            "profile_views": ["day", "lifetime"],
            "follower_count": ["day"],
            "audience_gender_age": ["lifetime"],
            "audience_city": ["lifetime"],
            "audience_country": ["lifetime"],
            "audience_locale": ["lifetime"],
            "saved": ["lifetime"],
        }

        insights_list = []

        for metric, valid_periods in metrics_periods.items():
            for period in valid_periods:
                try:
                    insights_data = self.client.graph.get_connections(
                        insta_id, "insights", metric=metric, period=period
                    )
                    if "data" in insights_data and len(insights_data["data"]) > 0:
                        for insight in insights_data["data"]:
                            insight_item = Insight(
                                name=insight["name"],
                                period=insight["period"],
                                values=insight["values"],
                                title=insight.get("title", ""),
                                description=insight.get("description", ""),
                                id=insight["id"],
                            )
                            insights_list.append(insight_item)
                except facebook.GraphAPIError as e:
                    pass

        logger.info(f"Retrieved {len(insights_list)} insights.")
        return insights_list
