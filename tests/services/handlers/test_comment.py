import pytest
from sage_meta.service.handlers import CommentHandler
from sage_meta.service.base import FacebookClient
from sage_meta.models import Comment, PostMention, CommentMention, ReplyMention
from tests.assets.token import get_access_token

@pytest.fixture
def comment_handler():
    access_token = get_access_token()
    client = FacebookClient(access_token=access_token)
    return CommentHandler(client)

class DummyResponse:
    def __init__(self, data=None):
        self._data = data or {}

    def raise_for_status(self):
        pass

    def json(self):
        return self._data

def test_get_instagram_comments(comment_handler, mocker):
    mocker.patch('requests.get', return_value=DummyResponse({
        "data": [
            {"id": "123", "text": "Nice post!", "username": "user1", "like_count": 10, "timestamp": "2023-07-31"}
        ]
    }))
    comments = comment_handler.get_instagram_comments("media_id")
    assert comments is not None
    assert len(comments) > 0
    assert isinstance(comments[0], Comment)
    assert comments[0].id == "123"

def test_get_post_mentions(comment_handler, mocker):
    mocker.patch('requests.get', return_value=DummyResponse({
        "mentioned_media": {
            "id": "media1", "media_type": "image", "media_url": "http://example.com", "caption": "Nice post!",
            "comments_count": 10, "like_count": 100, "timestamp": "2023-07-31", "username": "user1", "owner": "owner1"
        }
    }))
    mention = comment_handler.get_post_mentions("insta_id", "media_id")
    assert mention is not None
    assert isinstance(mention, PostMention)
    assert mention.id == "media1"

def test_get_comment_mentions(comment_handler, mocker):
    mocker.patch('requests.get', return_value=DummyResponse({
        "mentioned_comment": {
            "id": "comment1", "text": "Nice comment!", "like_count": 10, "timestamp": "2023-07-31", "username": "user1"
        }
    }))
    mention = comment_handler.get_comment_mentions("insta_id", "comment_id")
    assert mention is not None
    assert isinstance(mention, CommentMention)
    assert mention.id == "comment1"

def test_reply_to_mention(comment_handler, mocker):
    mocker.patch('requests.post', return_value=DummyResponse({
        "id": "reply1", "timestamp": "2023-07-31"
    }))
    reply = comment_handler.reply_to_mention("insta_id", "comment_id", "Test reply", "media_id")
    assert reply is not None
    assert isinstance(reply, ReplyMention)
    assert reply.id == "reply1"
