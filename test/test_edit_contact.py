__author__ = 'makarenok'

from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(first_name="editFirstName", middle_name="editMiddleName", last_name="editLastName",
                             nick="editNick", title="editTitleTest", company="editCompanyTest",
                             address="editAddressTest", tel_home="123", email="editTestMail@company"))
    app.session.logout()
