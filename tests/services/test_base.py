import pytest
from sage_meta.service.base import FacebookClient
from tests.assets.token import get_access_token

@pytest.fixture
def facebook_client():
    access_token = get_access_token()
    return FacebookClient(access_token=access_token)

class DummyGraphAPI:
    def get_object(self, *args, **kwargs):
        return {"id": "123", "name": "Test User", "email": "test@example.com"}

def test_facebook_client_initialization(facebook_client):
    assert facebook_client.graph_url == "https://graph.facebook.com/v20.0"
    assert facebook_client.graph is not None
    assert facebook_client.user is not None
    assert facebook_client.insta_business is None

def test_get_user_data(facebook_client):
    facebook_client.graph = DummyGraphAPI()
    facebook_client.get_user_data()
    assert facebook_client.user.id == "123"
    assert facebook_client.user.name == "Test User"
    assert facebook_client.user.email == "test@example.com"
