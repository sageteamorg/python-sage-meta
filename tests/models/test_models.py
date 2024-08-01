import pytest
from sage_meta.models import (
    Category,
    Insight,
    AccountInsight,
    Comment,
    Story,
    Media,
    InstagramAccount,
    FacebookPageData,
    UserData,
    PostMention,
    CommentMention,
    ReplyMention,
)

def test_category_creation():
    category = Category(id="1", name="CategoryName")
    assert category.id == "1"
    assert category.name == "CategoryName"

def test_insight_creation():
    insight = Insight(id="1", name="InsightName", period="day")
    assert insight.id == "1"
    assert insight.name == "InsightName"
    assert insight.period == "day"
    assert insight.values == []
    assert insight.title is None
    assert insight.description is None

def test_account_insight_creation():
    account_insight = AccountInsight(id="1", name="AccountInsightName", period="week")
    assert account_insight.id == "1"
    assert account_insight.name == "AccountInsightName"
    assert account_insight.period == "week"
    assert account_insight.values == []
    assert account_insight.title == ""
    assert account_insight.description == ""

def test_comment_creation():
    comment = Comment(id="123", text="Nice post!", username="user1", timestamp="2024-07-31")
    assert comment.id == "123"
    assert comment.text == "Nice post!"
    assert comment.username == "user1"
    assert comment.timestamp == "2024-07-31"
    assert comment.like_count is None
    assert comment.additional_data == {}

def test_story_creation():
    story = Story(
        id="1",
        media_type="image",
        media_url="http://example.com",
        timestamp="2024-07-31",
    )
    assert story.id == "1"
    assert story.media_type == "image"
    assert story.media_url == "http://example.com"
    assert story.timestamp == "2024-07-31"
    assert story.additional_data == {}

def test_media_creation():
    media = Media(
        id="1",
        caption="Caption",
        media_type="image",
        media_url=["http://example.com"],
        timestamp="2024-07-31",
    )
    assert media.id == "1"
    assert media.caption == "Caption"
    assert media.media_type == "image"
    assert media.media_url == ["http://example.com"]
    assert media.timestamp == "2024-07-31"
    assert media.like_count is None
    assert media.comments_count is None
    assert media.comments == []
    assert media.additional_data == {}

def test_instagram_account_creation():
    account = InstagramAccount(
        id="1",
        username="user1",
        follows_count=150,
        followers_count=1000,
        media_count=10,
    )
    assert account.id == "1"
    assert account.username == "user1"
    assert account.follows_count == 150
    assert account.followers_count == 1000
    assert account.media_count == 10
    assert account.profile_picture_url is None
    assert account.website is None
    assert account.biography is None
    assert account.media == []
    assert account.insights == []
    assert account.stories == []
    assert account.additional_data == {}

def test_facebook_page_data_creation():
    category = Category(id="1", name="CategoryName")
    account = InstagramAccount(
        id="1",
        username="user1",
        follows_count=150,
        followers_count=1000,
        media_count=10,
    )
    page_data = FacebookPageData(
        id="1",
        name="PageName",
        category="Category",
        access_token="token",
        category_list=[category],
        tasks=["task1"],
        instagram_business_account=account,
    )
    assert page_data.id == "1"
    assert page_data.name == "PageName"
    assert page_data.category == "Category"
    assert page_data.access_token == "token"
    assert page_data.category_list == [category]
    assert page_data.tasks == ["task1"]
    assert page_data.instagram_business_account == account
    assert page_data.additional_data == {}

def test_user_data_creation():
    page_data = FacebookPageData(
        id="1", name="PageName", category="Category", access_token="token"
    )
    user_data = UserData(
        id="1", name="UserName", email="user@example.com", pages=[page_data]
    )
    assert user_data.id == "1"
    assert user_data.name == "UserName"
    assert user_data.email == "user@example.com"
    assert user_data.pages == [page_data]
    assert user_data.additional_data == {}

def test_post_mention_creation():
    mention = PostMention(
        id="1",
        media_type="image",
        media_url="http://example.com",
        caption="Caption",
        comments_count=10,
        like_count=100,
        timestamp="2024-07-31",
        username="user1",
        owner="owner1",
    )
    assert mention.id == "1"
    assert mention.media_type == "image"
    assert mention.media_url == "http://example.com"
    assert mention.caption == "Caption"
    assert mention.comments_count == 10
    assert mention.like_count == 100
    assert mention.timestamp == "2024-07-31"
    assert mention.username == "user1"
    assert mention.owner == "owner1"
    assert mention.additional_data == {}

def test_comment_mention_creation():
    mention = CommentMention(
        id="1",
        text="Nice comment!",
        like_count=10,
        timestamp="2024-07-31",
        username="user1",
    )
    assert mention.id == "1"
    assert mention.text == "Nice comment!"
    assert mention.like_count == 10
    assert mention.timestamp == "2024-07-31"
    assert mention.username == "user1"
    assert mention.additional_data == {}

def test_reply_mention_creation():
    reply = ReplyMention(id="1", message="Reply message", timestamp="2024-07-31")
    assert reply.id == "1"
    assert reply.message == "Reply message"
    assert reply.timestamp == "2024-07-31"
    assert reply.additional_data == {}
