import pytest
from sage_meta.service.handlers import StoryHandler
from sage_meta.service.base import FacebookClient
from sage_meta.models import Story
from tests.assets.token import get_access_token

@pytest.fixture
def story_handler():
    access_token = get_access_token()
    client = FacebookClient(access_token=access_token)
    client.graph = DummyGraphAPI()
    return StoryHandler(client)

class DummyGraphAPI:
    def get_connections(self, user_id, connection_name, **kwargs):
        if connection_name == "stories":
            return {
                "data": [
                    {"id": "story1", "media_type": "image", "media_url": "http://example.com/story1.jpg", "timestamp": "2023-07-31"}
                ]
            }
        return {"data": []}

class DummyResponse:
    def __init__(self, data=None):
        self._data = data or {}

    def raise_for_status(self):
        pass

    def json(self):
        return self._data

def test_get_instagram_stories(story_handler):
    stories = story_handler.get_instagram_stories("insta_id")
    assert stories is not None
    assert len(stories) == 1
    assert isinstance(stories[0], Story)
    assert stories[0].id == "story1"
    assert stories[0].media_type == "image"
    assert stories[0].media_url == "http://example.com/story1.jpg"
    assert stories[0].timestamp == "2023-07-31"
