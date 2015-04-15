# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="firstName", middle_name="middleName", last_name="lastName",
                      nick="nick", title="titleTest", company="companyTest", address="addressTest",
                      tel_home="123", email="testMail@company")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(first_name="", middle_name="", last_name="",
#                      nick="", title="", company="", address="",
#                      tel_home="", email="")
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts)+1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
