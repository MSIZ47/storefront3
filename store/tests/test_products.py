import pytest
from model_bakery import baker
from rest_framework import status
from store.models import Product



@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/product/',product)
    return do_create_product



@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymouse_returns_401(self,api_client):
        #Arrange
        product = baker.make(Product)
        #Act
        response = api_client.post('/store/products/',product)
        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        print(product)

