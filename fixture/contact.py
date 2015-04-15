__author__ = 'makarenok'


from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nick)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.tel_home)
        # check email
        if contact.email is not None:
            self.change_field_value("email", contact.email)
        else:
            wd.find_element_by_name("email").clear()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creating
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@type='button'][@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit'][@title='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if self.check_url_home_page():
            wd.find_element_by_link_text("home").click()

    def return_home_page(self):
        wd = self.app.wd
        if self.check_url_home_page():
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def check_url_home_page(self):
        wd = self.app.wd
        return not wd.current_url == "http://localhost/addressbook/"

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for tr in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id_element = tr.find_element_by_name("selected[]").get_attribute("value")
                tds = tr.find_elements_by_tag_name('td')
                last_name = tds[1].text
                first_name = tds[2].text
                self.contact_cache.append(Contact(last_name=last_name, first_name=first_name, id=id_element))
        return list(self.contact_cache)
