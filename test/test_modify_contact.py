__author__ = 'makarenok'

from model.contact import Contact


def test_modify_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="testFirstName", middle_name="testMiddleName"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="New firstName")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_contact_middle_name(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="testFirstName", middle_name="testMiddleName"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(middle_name="New middleName"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts)== len(new_contacts)
