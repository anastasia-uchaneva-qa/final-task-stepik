import time
import pytest
from pages.product_page import ProductPage

#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#@pytest.mark.parametrize('promo_offer', ["0","1","2", "3", "4", "5", "6", "7", "8", "9"])
@pytest.mark.parametrize('promo_offer', ["0","1","2", "3", "4", "5", "6", "8", "9", pytest.param("7", marks=pytest.mark.xfail)])
def test_quiz(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_successful_message()
    page.should_be_message_with_price()
    page.check_price()
    page.check_name_of_book()
    #time.sleep(60)