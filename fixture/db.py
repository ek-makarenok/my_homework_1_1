__author__ = 'makarenok'
import mysql.connector
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 "
                           "from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                id = row[0]
                firstname = row[1]
                lastname = row[2]
                address = row[3]
                all_phones = '\n'.join(filter(None, row[4:8]))
                all_emails = '\n'.join(filter(None, row[-3:]))
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                    all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()