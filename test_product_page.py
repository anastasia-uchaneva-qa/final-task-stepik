import time
from pages.product_page import ProductPage

def test_quiz(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.solve_quiz_and_get_code()

def test_user_should_see_successful_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_successful_message()

def test_user_should_see_message_with_price(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_with_price()

def test_check_price(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.solve_quiz_and_get_code()
    page.check_price()

def test_check_name_of_book(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.solve_quiz_and_get_code()
    page.check_name_of_book()
    #time.sleep(60)