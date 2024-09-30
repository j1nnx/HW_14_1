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
        if type(self) is not type(other):
            raise TypeError
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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
            raise TypeError('Not a product')

    @property
    def products(self) -> Any:
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]

    def __str__(self) -> Any:
        return f"{self.name}, количество продуктов: {Category.product_count} шт."


# if __name__ == '__main__':
#     smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
#                              "S23 Ultra", 256, "Серый")
#     smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
#     smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
#
#     grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
#     grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
#
#     smartphone_sum = smartphone1 + smartphone2
#     print(smartphone_sum)
#
#     grass_sum = grass1 + grass2
#     print(grass_sum)
#
#     try:
#         invalid_sum = smartphone1 + grass1
#     except TypeError:
#         print("Возникла ошибка TypeError при попытке сложения")
#     else:
#         print("Не возникла ошибка TypeError при попытке сложения")
#
#     category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
#     category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])
#
#     category_smartphones.add_product(smartphone3)
#
#     print(category_smartphones.products)
#
#     print(Category.product_count)
#
#     try:
#         category_smartphones.add_product("Not a product")
#     except TypeError:
#         print("Возникла ошибка TypeError при добавлении не продукта")
#     else:
#         print("Не возникла ошибка TypeError при добавлении не продукта")
