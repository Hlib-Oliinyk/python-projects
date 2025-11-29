class Shop:
    def __init__(self, shop_name, store_type):
        self.valid = True

        if not isinstance(shop_name, str) or not shop_name.strip():
            self.valid = False
            self.shop_name = None
        else:
            self.shop_name = shop_name.strip()

        if not isinstance(store_type, str) or not store_type.strip():
            self.valid = False
            self.store_type = None
        else:
            self.store_type = store_type.strip()

        self.number_of_units = 0

        if not self.valid:
            print("Помилка: некоректні дані магазину")

    def describe_shop(self):
        if not self.valid:
            return
        print(f"Назва магазину: {self.shop_name}")
        print(f"Тип магазину: {self.store_type}")

    def open_shop(self):
        if not self.valid:
            return
        print(f"Магазин '{self.shop_name}' відкритий!")

    def set_number_of_units(self, number):
        if not self.valid:
            return
        if not isinstance(number, int) or number < 0:
            print("Помилка: кількість видів товару має бути додатнім цілим числом")
            return
        self.number_of_units = number

    def increment_number_of_units(self, increment):
        if not self.valid:
            return
        if not isinstance(increment, int) or increment < 0:
            print("Помилка: збільшення кількості має бути додатнім цілим числом")
            return
        self.number_of_units += increment


class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products=None):
        super().__init__(shop_name, store_type)
        if not self.valid:
            self.discount_products = []
            return

        if discount_products is None:
            self.discount_products = []
        elif isinstance(discount_products, list) and all(isinstance(p, str) for p in discount_products):
            self.discount_products = discount_products
        else:
            print("Помилка: discount_products має бути списком рядків")
            self.discount_products = []
            self.valid = False

    def get_discounts_products(self):
        if not self.valid:
            return
        if not self.discount_products:
            print("Список товарів зі знижками порожній")
            return
        print("Товари зі знижками:")
        for product in self.discount_products:
            print(f"- {product}")
