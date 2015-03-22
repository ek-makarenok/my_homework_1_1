from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper

__author__ = 'makarenok'


class Application:
    def __init__(self):
        # метод инициализирует фикстуру
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        # метод разрушает фикстуру
        self.wd.quit()