import json

import pytest

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    endpoint = "/api/category/"

    def test_get_all_categories(self, category_factory, api_client):
        category_factory.create_batch(4)

        response = api_client().get(self.endpoint)
        data = json.loads(response.content)
        assert response.status_code == 200
        assert len(data.get("data")) == 4


class TestBrandEndpoints:
    endpoint = "/api/brand/"

    def test_get_all_brands(self, brand_factory, api_client):
        brand_factory.create_batch(4)

        response = api_client().get(self.endpoint)
        data = json.loads(response.content)
        assert response.status_code == 200
        assert len(data.get("data")) == 4


class TestProductEndpoints:
    endpoint = "/api/product/"

    def test_get_all_products(self, product_factory, api_client):
        product_factory.create_batch(4)

        response = api_client().get(self.endpoint)
        data = json.loads(response.content)
        assert response.status_code == 200
        assert len(data.get("data")) == 4
