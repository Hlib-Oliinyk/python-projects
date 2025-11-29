from lab8_task8 import Shop, Discount

class TestShop:
    def test_valid_initialization(self):
        shop = Shop("MyShop", "Retail")
        assert shop.valid is True
        assert shop.shop_name == "MyShop"
        assert shop.store_type == "Retail"
        assert shop.number_of_units == 0

    def test_invalid_initialization(self):
        shop = Shop("", "")
        assert shop.valid is False
        assert shop.shop_name is None
        assert shop.store_type is None

    def test_describe_shop(self):
        shop = Shop("MyShop", "Retail")
        desc = shop.describe_shop()
        assert desc == "Назва магазину: MyShop\nТип магазину: Retail"
        shop_invalid = Shop("", "")
        assert shop_invalid.describe_shop() is None

    def test_open_shop(self):
        shop = Shop("MyShop", "Retail")
        msg = shop.open_shop()
        assert msg == "Магазин 'MyShop' відкритий!"
        shop_invalid = Shop("", "")
        assert shop_invalid.open_shop() is None

    def test_set_number_of_units(self):
        shop = Shop("MyShop", "Retail")
        err = shop.set_number_of_units(-1)
        assert err == "Помилка: кількість видів товару має бути додатнім цілим числом"
        err = shop.set_number_of_units("a")
        assert err == "Помилка: кількість видів товару має бути додатнім цілим числом"
        err = shop.set_number_of_units(10)
        assert err is None
        assert shop.number_of_units == 10

    def test_increment_number_of_units(self):
        shop = Shop("MyShop", "Retail")
        err = shop.increment_number_of_units(-5)
        assert err == "Помилка: збільшення кількості має бути додатнім цілим числом"
        err = shop.increment_number_of_units("a")
        assert err == "Помилка: збільшення кількості має бути додатнім цілим числом"
        shop.set_number_of_units(5)
        err = shop.increment_number_of_units(3)
        assert err is None
        assert shop.number_of_units == 8

class TestDiscount:
    def test_valid_discount_initialization(self):
        discount_shop = Discount("Shop", "Type", discount_products=["item1", "item2"])
        assert discount_shop.valid is True
        assert discount_shop.discount_products == ["item1", "item2"]

    def test_invalid_discount_products(self):
        discount_shop = Discount("Shop", "Type", discount_products=["valid", 33])
        assert discount_shop.valid is False
        assert discount_shop.discount_products == []

    def test_empty_discount_products(self):
        discount_shop = Discount("Shop", "Type", discount_products=[])
        message = discount_shop.get_discounts_products()
        assert message == "Список товарів зі знижками порожній"

    def test_get_discounts_products(self):
        discount_shop = Discount("Shop", "Type", discount_products=["item1", "item2"])
        expected = "Товари зі знижками:\n- item1\n- item2"
        assert discount_shop.get_discounts_products() == expected

    def test_get_discounts_products_invalid_shop(self):
        discount_shop = Discount("", "")
        assert discount_shop.get_discounts_products() is None
