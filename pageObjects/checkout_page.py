import time
from playwright.sync_api import expect

class Checkoutpage:

    def __init__(self, page):
        self.page = page

    def customer_info(self):
        self.page.get_by_placeholder("First Name").fill("Abcd")
        self.page.get_by_placeholder("Last Name").fill("xyz")
        self.page.get_by_placeholder("Zip/Postal Code").fill("60656")
        
        self.page.get_by_role("button", name="continue").click()
        self.page.get_by_role("button", name="finish").click()
        
        expect(self.page.get_by_text("Thank you for your order!")).to_be_visible()
