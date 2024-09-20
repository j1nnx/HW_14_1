class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_info: dict):
        return cls(product_info['name'], product_info['description'], product_info['price'], product_info['quantity'])


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []

        Category.category_count += 1

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError('Что-то не работает')

    @property
    def products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]


# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category("Смартфоны",
#                          "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
#
#     category1.add_product(product1)
#     category1.add_product(product2)
#     category1.add_product(product3)
#
#     print(category1.products)
#
#     product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
#     category1.add_product(product4)
#     print(category1.products)
#     print(Category.product_count)
#
#     new_product = Product.new_product(
#         {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#          "quantity": 5})
#     print(new_product.name)
#     print(new_product.description)
#     print(new_product.price)
#     print(new_product.quantity)
#
#     new_product.price = 800
#     print(new_product.price)
#     new_product.price = -100
#     print(new_product.price)
#     new_product.price = 0
#     print(new_product.price)
