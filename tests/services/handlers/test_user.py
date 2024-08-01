import pytest
from sage_meta.service.handlers import AccountHandler
from sage_meta.service.base import FacebookClient
from sage_meta.models import FacebookPageData, InstagramAccount
from tests.assets.token import get_access_token

@pytest.fixture
def account_handler():
    access_token = get_access_token()
    client = FacebookClient(access_token=access_token)
    client.graph = DummyGraphAPI()
    return AccountHandler(client)

class DummyGraphAPI:
    def get_connections(self, user_id, connection_name, **kwargs):
        if connection_name == "accounts":
            return {
                "data": [
                    {"id": "page1", "name": "Test Page", "category": "Business", "category_list": [], "tasks": ["ADMIN"], "access_token": "page_access_token"}
                ]
            }
        return {"data": []}

    def get_object(self, object_id, fields=None):
        if fields == "instagram_business_account":
            return {"instagram_business_account": {"id": "insta1"}}
        elif fields == "id,username,follows_count,followers_count,media_count,profile_picture_url,website,biography":
            return {
                "id": "insta1", "username": "testuser", "follows_count": 100, "followers_count": 200, "media_count": 50,
                "profile_picture_url": "http://example.com/profile.jpg", "website": "http://example.com", "biography": "Test Bio"
            }
        return {}

    def get(self, url, params=None, timeout=10):
        if "biography" in params["fields"]:
            return DummyResponse({"biography": "Test Bio", "website": "http://example.com"})
        return DummyResponse()

class DummyResponse:
    def __init__(self, data=None):
        self._data = data or {}

    def raise_for_status(self):
        pass

    def json(self):
        return self._data

def test_get_accounts(account_handler):
    accounts = account_handler.get_accounts()
    assert accounts is not None
    assert len(accounts) == 1
    assert isinstance(accounts[0], FacebookPageData)
    assert accounts[0].id == "page1"

def test_get_instagram_business_account(account_handler):
    page = FacebookPageData(
        id="page1",
        name="Test Page",
        category="Business",
        category_list=[],
        tasks=["ADMIN"],
        access_token="page_access_token",
        additional_data={}
    )
    insta_account = account_handler.get_instagram_business_account(page)
    assert insta_account is not None
    assert isinstance(insta_account, InstagramAccount)
    assert insta_account.id == "insta1"

def test_get_account_settings(account_handler, mocker):
    mocker.patch('requests.get', return_value=DummyResponse({"biography": "Test Bio", "website": "http://example.com"}))
    settings = account_handler.get_account_settings()
    assert settings is not None
