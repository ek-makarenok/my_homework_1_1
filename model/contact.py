__author__ = 'makarenok'


class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nick=None, title=None,
                 company=None, address=None, tel_home=None, email=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick = nick
        self.title = title
        self.company = company
        self.address = address
        self.tel_home = tel_home
        self.email = email