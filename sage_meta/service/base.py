import logging
from typing import List, Optional

import facebook

from sage_meta.models import FacebookPageData, UserData
from sage_meta.service.content import ContentPublishing
from sage_meta.service.handlers import (
    AccountHandler,
    CommentHandler,
    HashtagHandler,
    MediaHandler,
    StoryHandler,
)

logger = logging.getLogger(__name__)


class FacebookClient:
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.graph_url = "https://graph.facebook.com/v20.0"
        self.graph = facebook.GraphAPI(access_token=access_token, version="3.1")
        self.user: Optional[UserData] = None
        self.insta_business = None
        self.pages: List[FacebookPageData] = []
        self.get_user_data()
        self.account_handler: AccountHandler = AccountHandler(self)
        self.media_handler: MediaHandler = MediaHandler(self)
        self.comment_handler: CommentHandler = CommentHandler(self)
        self.story_handler: StoryHandler = StoryHandler(self)
        self.hashtag_handler: HashtagHandler = HashtagHandler(self)
        self.content_publisher: ContentPublishing = ContentPublishing(self)

    def get_user_data(self) -> None:
        logger.debug("Fetching user data.")
        try:
            obj = self.graph.get_object("me", fields="id,name,email")
            additional_data = {
                k: v for k, v in obj.items() if k not in {"id", "name", "email"}
            }
            self.user = UserData(
                id=obj.get("id"),
                name=obj.get("name"),
                email=obj.get("email"),
                additional_data=additional_data,
            )
            logger.info("Retrieved user data: %s", self.user.id)
        except facebook.GraphAPIError as e:
            logger.error("Error fetching user data: %s", e)
            raise
