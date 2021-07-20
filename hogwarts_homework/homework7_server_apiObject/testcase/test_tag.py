import json
import pytest
import yaml
import logging
from jsonpath import jsonpath
from hogwarts_homework.homework7_server_apiObject.apiObject.tag.tag import Tag

class Test_Tag():
    def setup_class(self):
        self.tag = Tag('i8lbbMoby8YP1nJoDJuhT8Xc52-PRfB-vrjSTDcs1YM')
        self.tag.clear_whole_tag()

    def test_get_whole_tag(self):
        r = self.tag.get_whole_tag_list()
        logging.info(json.dumps(r.json(), indent=2, ensure_ascii=False))

    def test_add_tag(self):
        self.tag.clear_whole_tag()
        r = self.tag.add_tag_name("group1")
        assert r.json()['errcode'] == 0
        r = self.tag.get_whole_tag_list()
        assert 'group1' in [i['group_name'] for i in r.json()['tag_group']]

        r = self.tag.add_tag_name("group2", [{"name": "label1"}, {"name": "label2"}])
        assert r.json()['errcode'] == 0
        r = self.tag.get_whole_tag_list()
        assert r.json()["tag_group"][1]["tag"][0]["name"] == "label1"
        l = jsonpath(r.json(), '$..tag[*].name')
        assert 'label1' in l and 'label2' in l

    def test_delete_tag(self):
        self.tag.clear_whole_tag()
        r = self.tag.add_tag_name("group1")
        assert r.json()['errcode'] == 0
        r = self.tag.get_whole_tag_list()
        assert r.json()["tag_group"][0]["group_name"] == "group1"
        r = self.tag.del_tag_by_name(groupName = "group1")
        assert r['errcode'] == 0
        r = self.tag.get_whole_tag_list()
        assert r.json()["tag_group"] == []

    @pytest.mark.parametrize("tagNameOld, groupNameOld, newName, newOrder", yaml.safe_load(open('yaml/edit_tag_success.yaml', encoding = 'utf - 8')))
    def test_edit_tag(self, tagNameOld, groupNameOld, newName, newOrder):
        self.tag.clear_whole_tag()
        r = self.tag.add_tag_name("group", [{"name": "label1"}])
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

    def test_smoke_flow(self):
        self.tag.clear_whole_tag()
        r = self.tag.add_tag_name("group1", [{"name": "label1"}])
        assert r.json()['errcode'] == 0
        r = self.tag.edit_tag_name(tagNameOld='label1', newName='label1_bak')
        assert r.json()['errcode'] == 0

        r = self.tag.del_tag_by_name(tagName = "label1_bak")
        assert r['errcode'] == 0
        r = self.tag.get_whole_tag_list()
        assert r.json()["tag_group"] == []




