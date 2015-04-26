__author__ = 'makarenok'

from random import randrange
import re


def test_info_on_home_page(app):
    len_contact = len(app.contact.get_contact_list())
    index = randrange(len_contact)
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    list_contact_phones = [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]
    not_none_list_contact_phones = filter(lambda x: x is not None, list_contact_phones)
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), not_none_list_contact_phones)))


def merge_emails_like_on_home_page(contact):
    list_contact_emails = [contact.email, contact.email2, contact.email3]
    not_none_list_contact_emails = filter(lambda x: x is not None, list_contact_emails)
    return "\n".join(filter(lambda x: x != "", not_none_list_contact_emails))