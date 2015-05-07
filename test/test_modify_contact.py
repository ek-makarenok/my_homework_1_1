__author__ = 'makarenok'

from model.contact import Contact
import random


def test_modify_contact_first_name(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testFirstName", middlename="testMiddleName"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact = Contact(firstname="New firstName")
    new_contact.id = contact.id
    app.contact.modify_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    for i, old_contact in enumerate(old_contacts):
        if old_contact.id == contact.id:
            old_contacts[i] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

# def test_modify_contact_middle_name(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="testFirstName", middle_name="testMiddleName"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(middle_name="New middleName"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts)== len(new_contacts)
