# Stub for sage_meta.service.content

from typing import List, Optional, Dict

class ContentPublishing:
    def __init__(self, client: "FacebookClient") -> None: ...
    def publish_photo(self, image_url: str, caption: str) -> dict: ...
    def publish_video(self, video_url: str, caption: str) -> dict: ...
    def upload_video(self, video_url: str, caption: str) -> Optional[str]: ...
    def publish_carousel(self, media_urls: List[str], caption: str) -> dict: ...
    def get_media_status(self, media_id: str) -> dict: ...
    def put_comment(self, post_id: str, message: str) -> dict: ...
    def reply_to_comment(self, comment_id: str, message: str) -> dict: ...
    def publish_story(self, image_url: str) -> dict: ...