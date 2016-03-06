# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):

    fixture = Application()
    request.addfinalizer(fixture.distroy)
    return fixture

def test_(app):

        app.session.login(username="admin", password="secret")
        app.create_group(Group(name="fffff", header="eeeee", footer="ggggg"))
        app.session.logout()

def test_emptygroup(app):

        app.session.login(username="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.session.logout()
