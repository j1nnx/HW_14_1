from typing import Any

import pytest

from src.main import Category, Product


@pytest.fixture()
def test_product() -> Any:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product_init(test_product: Any) -> Any:
    assert test_product.name == "Samsung Galaxy S23 Ultra"
    assert test_product.description == "256GB, Серый цвет, 200MP камера"
    assert test_product.price == 180000.0
    assert test_product.quantity == 5


@pytest.fixture()
def test_category() -> Any:
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    )
    return category2


def test_category_init(test_category: Any) -> Any:
    assert test_category.name == "Телевизоры"
    assert (
        test_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )


@pytest.fixture()
def test_new_product():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    return new_product


def test_new_product_init(test_new_product):
    assert test_new_product.name == "Samsung Galaxy S23 Ultra"
    assert test_new_product.description == "256GB, Серый цвет, 200MP камера"
    assert test_new_product.price == 180000.0
    assert test_new_product.quantity == 5

