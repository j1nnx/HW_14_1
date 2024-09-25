from typing import Any

from src.main import Category, Product

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


def test_str_product() -> Any:
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(product3) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3],
)


def test_str_category() -> Any:
    assert str(category1) == "Смартфоны, количество продуктов: 0 шт."


expected_products = [
    "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
    "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
    "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
]


def test_method_category() -> Any:
    assert category1.products == expected_products


def test_add_init() -> Any:
    assert (product1 + product2) == (180000.0 * 5 + 210000.0 * 8)
    assert (product1 + product3) == (180000.0 * 5 + 31000.0 * 14)
    assert (product2 + product3) == (210000.0 * 8 + 31000.0 * 14)
