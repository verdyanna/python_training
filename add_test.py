# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from application import Application


@pytest.fixture
def app(request):

    fixture = Application()
    request.addfinalizer(fixture.distroy)
    return fixture

def test_(app):

        app.login(username="admin", password="secret")
        app.create_group(Group(name="fffff", header="eeeee", footer="ggggg"))
        app.logout()

def test_emptygroup(app):

        app.login(username="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()
