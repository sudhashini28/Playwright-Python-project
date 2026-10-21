import time

class Loginmainpage:

    def __init__(self, page, login_usernames):
        self.page = page
        self.login_usernames = login_usernames

    def Navigate_url(self):
        self.page.goto("https://www.saucedemo.com/")
    

    def loginusernamesandpasswords(self):
        self.page.get_by_placeholder("Username").fill(self.login_usernames["LoginName"])
        self.page.get_by_placeholder("Password").fill(self.login_usernames["LoginPassword"])
        self.page.locator('[data-test="login-button"]').click()


    