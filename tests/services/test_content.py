import pytest
from sage_meta.service.content import ContentPublishing
from sage_meta.service.base import FacebookClient

from tests.assets.token import get_access_token

@pytest.fixture
def content_publisher():
    access_token = get_access_token()
    client = FacebookClient(access_token=access_token)
    client.graph = DummyGraphAPI()
    return ContentPublishing(client)

class DummyGraphAPI:
    def put_object(self, parent_object, connection_name, **kwargs):
        if connection_name == "media":
            if "image_url" in kwargs:
                return {"id": "media1"}
            if "media_type" in kwargs and kwargs["media_type"] == "CAROUSEL":
                return {"id": "carousel"}
        elif connection_name == "media_publish":
            return {"id": "media_publish1"}
        elif connection_name == "comments":
            return {"id": "comment_id"}
        elif connection_name == "replies":
            return {"id": "reply_id"}
        return {"id": "unknown"}

    def put_comment(self, post_id, message):
        return {"id": "comment_id"}

    def get_object(self, *args, **kwargs):
        return {"id": "123", "name": "Test User", "email": "test@example.com"}

    def get(self, url, params=None, timeout=10):
        return DummyResponse()

class DummyResponse:
    def json(self):
        return {"status_code": "finished", "status": "complete"}

def test_publish_photo(content_publisher):
    response = content_publisher.publish_photo(
        "your_photo_url", "Test Caption"
    )
    assert response is not None
    assert "id" in response



def test_publish_carousel(content_publisher):
    response = content_publisher.publish_carousel(
        ["your_photo_url1", "your_photo_url2"],
        "Test Caption",
    )
    assert response is not None
    assert "id" in response


def test_put_comment(content_publisher):
    response = content_publisher.put_comment("post_id", "Test comment")
    assert response == {"id": "comment_id"}

def test_reply_to_comment(content_publisher):
    response = content_publisher.reply_to_comment("comment_id", "Test reply")
    assert response is not None

def test_publish_story(content_publisher):
    response = content_publisher.publish_story("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS75ebrwvgVW5Ks_oLfCbG8Httf3_9g-Ynl_Q&s")
    assert response is not None
