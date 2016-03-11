# -*- coding: utf-8 -*-

from model.group import Group

def test_(app):
        old_groups = app.group.get_group_list()
        app.group.create(Group(name="fffff", header="eeeee", footer="ggggg"))
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)


def test_emptygroup(app):
        old_groups = app.group.get_group_list()
        app.group.create(Group(name="", header="", footer=""))
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)

