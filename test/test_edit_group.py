__author__ = 'makarenok'

from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="edit_group", header="edit_group_header", footer="edit_group_footer"))
    app.session.logout()
