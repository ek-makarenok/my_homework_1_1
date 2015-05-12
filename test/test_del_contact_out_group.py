# -*- coding: utf-8 -*-
__author__ = 'makarenok'

from model.contact import Contact
from model.group import Group
import random


def test_del_contact_out_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="testFirstName", lastname="testLastName"))
    group = random.choice(db.get_group_list())
    contact = random.choice(db.get_contact_list())
    contacts_in_group = db.get_contacts_in_group(group)
    if len(contacts_in_group) == 0:
        app.contact.add_contact_in_group(contact, group)
    contact_in_group = random.choice(db.get_contacts_in_group(group))
    app.group.del_contact_out_group(contact_in_group, group)
