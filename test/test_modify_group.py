__author__ = 'makarenok'

from model.group import Group


def test_modify_group_name(app):
    app.group.check_group(Group(name="test"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    app.group.check_group(Group(name="test"))
    app.group.modify_first_group(Group(header="New header"))

