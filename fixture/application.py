from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper

__author__ = 'makarenok'


class Application:
    def __init__(self):
        # метод инициализирует фикстуру
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        # метод разрушает фикстуру
        self.wd.quit()