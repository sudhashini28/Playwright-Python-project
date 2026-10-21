import pytest
import json
import time
from playwright.sync_api import Page, Playwright, expect
from pageObjects.login_page import Loginmainpage
from pageObjects.checkout_page import Checkoutpage
from pageObjects.inventory_page import Inventorypage

#convert json to phython
with open('loginDetails/login_info.json') as f:
    user_data = json.load(f)
    print(user_data)
    login_userinfo = user_data['login_usernames']

@pytest.mark.parametrize('login_usernames', login_userinfo)
def test_Mainframework(login_usernames, browser_instance):

    login_page = Loginmainpage(browser_instance, login_usernames)
    login_page.Navigate_url()
    login_page.loginusernamesandpasswords()

    inventory_page = Inventorypage(browser_instance)
    inventory_page.sort_by_price_low_to_high()
    inventory_page.Adding_itemstocart()
    inventory_page.Navigate_tocheckout()

    checkout_page = Checkoutpage(browser_instance)
    checkout_page.customer_info()

















def test_sample(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    time.sleep(5)
    page.get_by_placeholder("Username").fill("standard_user")
    time.sleep(1)
    page.get_by_placeholder("Password").fill("secret_sauce")
    time.sleep(1)
    page.get_by_role("button", name="Login").click()
    time.sleep(1)
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    time.sleep(1)
    page.locator("#add-to-cart-sauce-labs-bolt-t-shirt").click()
    time.sleep(1)
    playwright.selectors.set_test_id_attribute("data-test")
    page.get_by_test_id("add-to-cart-test.allthethings()-t-shirt-(red)").click()
    time.sleep(1)
    page.evaluate("window.scrollTo(0, 0)")
    time.sleep(1)
    page.locator(".shopping_cart_badge").click()
    time.sleep(1)
    page.get_by_test_id("checkout").click()
    time.sleep(1)
    page.get_by_placeholder("First Name").fill("Abcd")
    page.get_by_placeholder("Last Name").fill("xyz")
    page.get_by_placeholder("Zip/Postal Code").fill("60656")
    time.sleep(1)
    page.get_by_role("button", name="continue").click()
    time.sleep(1)
    page.get_by_role("button", name="finish").click()
    time.sleep(1)
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
    browser.close()