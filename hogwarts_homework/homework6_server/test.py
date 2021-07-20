import json
import pytest
import yaml
from hogwarts_homework.homework6_server.tag import Tag


class Test_WeChat():

    def setup_class(self):
        self.tag = Tag()

    def test_get_whole_tag(self):
        r = self.tag.get_whole_tag_list()
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))

    def test_add_tag(self):
        self.tag.clear_whole_tag()
        r = self.tag.add_tag_name("group1")
        assert r.json()['errcode'] == 0
        r = self.tag.get_whole_tag_list()
        assert r.json()["tag_group"][0]["group_name"] == "group1"

        r = self.tag.add_tag_name("group2", ["label1", "label2"])
        assert r.json()['errcode'] == 0
        r = self.tag.get_whole_tag_list()
        assert r.json()["tag_group"][1]["tag"][0]["name"] == "label1"

    def test_delete_tag(self):
        self.tag.clear_whole_tag()
        r = self.tag.add_tag_name("group1")
        assert r.json()['errcode'] == 0
        r = self.tag.get_whole_tag_list()
        assert r.json()["tag_group"][0]["group_name"] == "group1"
        r = self.tag.del_tag_by_name(groupName = "group1")
        print(r['errcode'] == 0)
        r = self.tag.get_whole_tag_list()
        assert r.json()["tag_group"] == []

    @pytest.mark.parametrize("tagNameOld, groupNameOld, newName, newOrder", yaml.safe_load(open('yaml/edit_tag_success.yaml', encoding = 'utf - 8')))
    def test_edit_tag(self, tagNameOld, groupNameOld, newName, newOrder):
        self.tag.clear_whole_tag()
        r = self.tag.add_tag_name("group", ["label1"])
        assert r.json()['errcode'] == 0
        r = self.tag.get_whole_tag_list()
        assert r.json()["tag_group"][0]["tag"][0]["name"] == "label1"
        r = self.tag.edit_tag_name(tagNameOld = tagNameOld, groupNameOld = groupNameOld, newName = newName, newOrder = newOrder)
        assert r.json()['errcode'] == 0
        r = self.tag.get_whole_tag_list()
        if tagNameOld is not None:
            assert r.json()["tag_group"][0]["tag"][0]["name"] == newName
            if newOrder is not None:
                assert r.json()["tag_group"][0]["tag"][0]["order"] == newOrder
        elif groupNameOld is not None:
            assert r.json()["tag_group"][0]["group_name"] == newName
            if newOrder is not None:
                assert r.json()["tag_group"][0]["order"] == newOrder






