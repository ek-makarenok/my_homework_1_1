# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="firstName", middle_name="middleName", last_name="lastName",
                               nick="nick", title="titleTest", company="companyTest", address="addressTest",
                               tel_home="123", email="testMail@company"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="", middle_name="", last_name="",
                               nick="", title="", company="", address="",
                               tel_home="", email=""))
    app.session.logout()
