__author__ = 'makarenok'

from model.contact import Contact


def test_delete_first_contact(app):
    app.contact.check_contact(Contact(first_name="testFirstName", last_name="testLastName"))
    app.contact.delete_first_contact()
