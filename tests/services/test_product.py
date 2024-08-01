import pytest
from dotenv import load_dotenv
import os

from sage_meta.service.product import InstagramProductTagging
from tests.assets.token import get_access_token

@pytest.fixture
def instagram_product_tagging():
    access_token = get_access_token()
    return InstagramProductTagging(access_token=access_token)

class DummyResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return {"id": "dummy_id", "product_tags": "tags", "copyright_check_status": "clear", "copyright_check_information": "clear"}

@pytest.fixture
def mock_requests(mocker):
    return mocker.patch('requests.post', return_value=DummyResponse())

def test_create_tagged_container(instagram_product_tagging, mock_requests):
    response = instagram_product_tagging.create_tagged_container(
        ig_user_id="12345",
        media_type="IMAGE",
        media_url="https://example.com/image.jpg",
        product_tags=[{"product_id": "123"}],
        caption="Test Caption"
    )
    assert response is not None
    assert "id" in response

def test_publish_media(instagram_product_tagging, mock_requests):
    response = instagram_product_tagging.publish_media(
        ig_user_id="12345",
        creation_id="dummy_id"
    )
    assert response is not None
    assert "id" in response

def test_get_product_tags(instagram_product_tagging, mocker):
    mocker.patch('requests.get', return_value=DummyResponse())
    response = instagram_product_tagging.get_product_tags("dummy_media_id")
    assert response is not None
    assert "product_tags" in response

def test_delete_product_tags(instagram_product_tagging, mocker):
    mocker.patch('requests.delete', return_value=DummyResponse())
    response = instagram_product_tagging.delete_product_tags("dummy_media_id")
    assert response is not None
    assert "id" in response

def test_update_product_tags(instagram_product_tagging, mock_requests):
    response = instagram_product_tagging.update_product_tags(
        media_id="dummy_media_id",
        product_tags=[{"product_id": "123"}]
    )
    assert response is not None
    assert "id" in response

def test_get_catalogs(instagram_product_tagging, mocker):
    mocker.patch('requests.get', return_value=DummyResponse())
    response = instagram_product_tagging.get_catalogs("12345")
    assert response is not None
    assert "id" in response

def test_get_eligible_products(instagram_product_tagging, mocker):
    mocker.patch('requests.get', return_value=DummyResponse())
    response = instagram_product_tagging.get_eligible_products("12345", "catalog_id", "query")
    assert response is not None
    assert "id" in response

def test_create_catalog(instagram_product_tagging, mock_requests):
    response = instagram_product_tagging.create_catalog(
        business_id="12345",
        catalog_name="Test Catalog"
    )
    assert response is not None
    assert "id" in response
