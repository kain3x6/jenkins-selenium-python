from time import sleep

import pytest
from page_objects.greencard_page import GreenCardPage

class TestProducts:

    @pytest.mark.smoke
    @pytest.mark.parametrize("product", ["Brocolli - 1 Kg", 'Cauliflower - 1 Kg'])
    @pytest.mark.timeout(300)
    def test_add_product(self, product, browser_init):

        driver = browser_init

        greencard_page = GreenCardPage(driver)
        greencard_page.navigate()
        greencard_page.add_to_cart(product)
        greencard_page.open_cart_list()
        greencard_page.proceed_to_checkout()
        sleep(3)
        assert True
