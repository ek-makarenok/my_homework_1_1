# -*- coding: utf-8 -*-
__author__ = 'makarenok'

from model.contact import Contact
import random


def test_add_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="testFirstName", lastname="testLastName"))
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    contact = random.choice(old_contacts)
    group = random.choice(old_groups)
    app.contact.add_contact_in_group(contact, group)

