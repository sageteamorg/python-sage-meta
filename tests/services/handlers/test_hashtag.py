import pytest
from sage_meta.service.handlers import HashtagHandler
from sage_meta.service.base import FacebookClient
from tests.assets.token import get_access_token
@pytest.fixture
def hashtag_handler():
    access_token = get_access_token()
    client = FacebookClient(access_token=access_token)
    return HashtagHandler(client)

class DummyResponse:
    def __init__(self, data=None):
        self._data = data or {}

    def raise_for_status(self):
        pass

    def json(self):
        return self._data

def test_search_hashtag(hashtag_handler, mocker):
    mocker.patch('requests.get', return_value=DummyResponse({
        "data": [{"id": "12345"}]
    }))
    hashtag_id = hashtag_handler.search_hashtag("insta_id", "test")
    assert hashtag_id == "12345"

def test_get_hashtag_info(hashtag_handler, mocker):
    mocker.patch('requests.get', return_value=DummyResponse({
        "id": "12345", "name": "test", "media_count": 100
    }))
    info = hashtag_handler.get_hashtag_info("12345")
    assert info is not None
    assert info["id"] == "12345"

def test_get_recent_media(hashtag_handler, mocker):
    mocker.patch('requests.get', return_value=DummyResponse({
        "data": [
            {"id": "123", "caption": "Nice post!", "media_type": "IMAGE", "media_url": "http://example.com", "permalink": "http://example.com/permalink"}
        ]
    }))
    media = hashtag_handler.get_recent_media("12345", "insta_id")
    assert media is not None
    assert "data" in media
    assert len(media["data"]) > 0

def test_get_top_media(hashtag_handler, mocker):
    mocker.patch('requests.get', return_value=DummyResponse({
        "data": [
            {"id": "123", "media_type": "IMAGE", "comments_count": 10, "like_count": 100}
        ]
    }))
    top_media = hashtag_handler.get_top_media("12345", "insta_id")
    assert top_media is not None
    assert "data" in top_media
    assert len(top_media["data"]) > 0
