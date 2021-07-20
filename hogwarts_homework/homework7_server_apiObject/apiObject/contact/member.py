import json
import logging

from jsonpath import jsonpath

from hogwarts_homework.homework7_server_apiObject.wework_api import Wework

class Member(Wework):
    def add_member(self, userid, name, mobile, department):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/create',
            'method': 'post',
            'params': {'access_token': self.access_token},
            'json': {
                'userid': userid,
                'name': name,
                'mobile': mobile,
                'department': department
            }
        }
        logging.info(json.dumps(data, indent = 2, ensure_ascii = False))
        return self.request(data)

    def get_member(self, userID):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/get',
            'method': 'get',
            'params': {'access_token': self.access_token,
                       'userid': userID}
        }
        return self.request(data)

    def del_member(self, userID):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/delete',
            'method': 'get',
            'params': {'access_token': self.access_token,
                       'userid': userID}
        }
        return self.request(data)

    def get_depart_member(self, departID, fetch_child = 0):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist',
            'method': 'get',
            'params': {'access_token': self.access_token,
                       'department_id': departID,
                       'fetch_child': fetch_child}
        }
        return self.request(data)

    def clear_depart_member_list(self,departID, fetch_child = 0):
        r = self.get_depart_member(departID, fetch_child)
        logging.info(r.json())
        l = jsonpath(r.json(), '$..userlist[*].userid')
        logging.info(l)
        if l == False:
            return {'errcode': 0, 'errmsg': 'department has no member'}
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete',
            'method': 'post',
            'params': {'access_token': self.access_token},
            'json': {
                'useridlist': l
            }
        }
        return self.request(data).json()
