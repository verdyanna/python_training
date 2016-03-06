# -*- coding: utf-8 -*-

from model.group import Group

def test_(app):

        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="fffff", header="eeeee", footer="ggggg"))
        app.session.logout()

def test_emptygroup(app):

        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="", header="", footer=""))
        app.session.logout()
