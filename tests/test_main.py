from typing import Any

from src.main import Category, Product, Smartphone, LawnGrass

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


smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                        "S23 Ultra", 256, "Серый")


def test_smarthone_init() -> Any:
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"


lawn_grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия",
                       "7 дней", "Зеленый")


def test_lawngrass_init() -> Any:
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"


def test_product_creation_with_zero_quantity():
    try:
        product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)
        print("Тест не пройден: исключение не выброшено")
    except ValueError as e:
        assert str(e) == "Товар с нулевым количеством не может быть добавлен", "Неверное сообщение об ошибке"
        print("Тест пройден: выброшено исключение ValueError")


def test_category_average_price_no_products():
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0, "Средний ценник для пустой категории должен быть 0"
    print("Тест пройден: средний ценник для пустой категории равен 0")