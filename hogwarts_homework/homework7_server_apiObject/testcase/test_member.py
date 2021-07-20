import json
import logging
import pytest
import yaml

from hogwarts_homework.homework7_server_apiObject.apiObject.contact.member import Member


class Test_Member():
    def setup_class(self):
        self.mem = Member('_yM2Jfo3ys0NjMdrY3RcqD54S3sDFIQnA0DkUfhYcmc')

    def setup(self):
        r = self.mem.clear_depart_member_list(2)
        assert r['errcode'] == 0

    @pytest.mark.parametrize('userid, name, mobile, department',
                              yaml.safe_load(open('yaml/add_member_success.yaml', encoding = 'utf-8')))
    def test_add_member(self, userid, name, mobile, department):
        r = self.mem.add_member(userid, name, mobile, department)
        assert r.json()['errcode'] == 0
        logging.info(r.json())
        r = self.mem.get_member(userid)
        logging.info(json.dumps(r.json(), ensure_ascii=False, indent=2))
        assert r.json()['userid'] == userid
        assert r.json()['mobile'] == mobile
        assert department in r.json()['department']



