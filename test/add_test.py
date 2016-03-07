# -*- coding: utf-8 -*-

from model.group import Group

def test_(app):
        app.group.create(Group(name="fffff", header="eeeee", footer="ggggg"))


def test_emptygroup(app):
        app.group.create(Group(name="", header="", footer=""))

