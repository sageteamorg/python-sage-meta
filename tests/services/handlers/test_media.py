import pytest
from sage_meta.service.handlers import MediaHandler
from sage_meta.service.base import FacebookClient
from sage_meta.models import Media, Insight
from tests.assets.token import get_access_token

@pytest.fixture
def media_handler():
    access_token = get_access_token()
    client = FacebookClient(access_token=access_token)
    client.graph = DummyGraphAPI()
    return MediaHandler(client)

class DummyGraphAPI:
    def get_connections(self, insta_id, connection_name, **kwargs):
        if connection_name == "media":
            return {
                "data": [
                    {"id": "media1", "caption": "Nice post!", "media_type": "IMAGE", "media_url": "http://example.com", "timestamp": "2023-07-31", "like_count": 100, "comments_count": 10}
                ]
            }
        elif connection_name == "insights":
            return {
                "data": [
                    {"name": "impressions", "period": "day", "values": [1, 2, 3], "id": "insight1"}
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

def test_get_instagram_media(media_handler):
    media = media_handler.get_instagram_media("insta_id")
    assert media is not None
    assert len(media) == 1
    assert isinstance(media[0], Media)
    assert media[0].id == "media1"

def test_get_instagram_insights(media_handler):
    insights = media_handler.get_instagram_insights("insta_id")
    assert insights is not None
    assert len(insights) == 12
    assert isinstance(insights[0], Insight)
    assert insights[0].id == "insight1"
