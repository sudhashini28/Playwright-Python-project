
class Inventorypage:

    def __init__(self, page):
        self.page = page

    def sort_by_price_low_to_high(self):
        self.page.locator(".product_sort_container").select_option("lohi")

    def Adding_itemstocart(self):
        self.page.locator('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
        self.page.locator("#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.page.locator("#add-to-cart-sauce-labs-backpack").click()
        
    def Navigate_tocheckout(self):
        #self.page.evaluate("window.scrollTo(0, 0)")
        self.page.locator(".shopping_cart_badge").click()
        self.page.evaluate("window.scrollBy(0, 500)")
        self.page.locator("#checkout").click()
        