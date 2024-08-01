import pytest
from sage_meta.service.copyright import CopyrightManager
from tests.assets.token import get_access_token

@pytest.fixture
def copyright_manager():
    access_token = get_access_token()
    return CopyrightManager(access_token=access_token)

class DummyResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return {"copyright_check_status": "clear", "copyright_check_information": "clear"}

def test_check_copyright_status_unpublished(copyright_manager, mocker):
    mocker.patch('requests.get', return_value=DummyResponse())
    response = copyright_manager.check_copyright_status_unpublished("container_id")
    assert response is not None
    assert "copyright_check_status" in response

def test_check_copyright_status_published(copyright_manager, mocker):
    mocker.patch('requests.get', return_value=DummyResponse())
    response = copyright_manager.check_copyright_status_published("media_id")
    assert response is not None
    assert "copyright_check_information" in response
