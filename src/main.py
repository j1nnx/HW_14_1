from typing import Any


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> Any:
        return self.__price

    def price_(self, value: float) -> Any:
        if value <= 0:
            return "Цена не должна быть нулевая или отрицательная"
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_info: dict) -> Any:
        return cls(product_info["name"], product_info["description"], product_info["price"], product_info["quantity"])

    def __str__(self) -> Any:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        self.product_count = len(self.__products)

        Category.category_count += 1

    def add_product(self, product: Product) -> Any:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Что-то не работает")


    @property
    def products(self) -> Any:
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]

    def __str__(self) -> Any:
        return f"{self.name}, количество продуктов: {Category.product_count} шт."


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
