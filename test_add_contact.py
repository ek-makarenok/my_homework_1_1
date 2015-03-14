# -*- coding: utf-8 -*-

import pytest
from application import Application
from contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="firstName", middle_name="middleName", last_name="lastName",
                               nick="nick", title="titleTest", company="companyTest", address="addressTest",
                               tel_home="123", email="testMail@company"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="", middle_name="", last_name="",
                               nick="", title="", company="", address="",
                               tel_home="", email=""))
    app.logout()
