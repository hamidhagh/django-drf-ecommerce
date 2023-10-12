import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import (
    AttributeFactory,
    AttributeValueFactory,
    CategoryFactory,
    ProductFactory,
    ProductImageFactory,
    ProductLineAttributeValueFactory,
    ProductLineFactory,
    ProductTypeFactory,
    BrandFactory
)

register(CategoryFactory)
register(ProductFactory)
register(ProductLineFactory)
register(ProductImageFactory)
register(ProductTypeFactory)
register(AttributeValueFactory)
register(AttributeFactory)
register(ProductLineAttributeValueFactory)
register(BrandFactory)


@pytest.fixture
def api_client():
    return APIClient
