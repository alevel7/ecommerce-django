import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(test, category_factory):
        # arrange
        x = category_factory(name="test_category")
        print(x)
        assert x.__str__() == "test_category"


class TestProductModel:
    def test_str_method(test, product_factory):
        # arrange
        x = product_factory(name="test_product")
        assert x.__str__() == "test_product"


class TestBrandModel:
    def test_str_method(test, brand_factory):
        # arrange
        x = brand_factory(name="test_brand")
        # act
        # assert
        assert x.__str__() == "test_brand"
