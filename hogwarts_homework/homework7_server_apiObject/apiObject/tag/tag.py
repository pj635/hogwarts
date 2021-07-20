import time

from hogwarts_homework.homework7_server_apiObject.wework_api import Wework
import logging

logging.basicConfig(level = logging.INFO, format = '%(filename)s:%(lineno)d[%(levelname)s] ')
logger = logging.getLogger(__name__)


class Tag(Wework):
    def get_whole_tag_list(self):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            'method': 'post',
            'params': {
                'access_token': self.access_token
            }
        }
        r = self.request(data)
        #logger.info(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def get_tag_id_by_name(self, tagName = None, groupName = None):
        if tagName == None and groupName == None:
            return(None, None)
        else:
            r = self.get_whole_tag_list()
            tag_list =  r.json()["tag_group"]
            for i in tag_list:
                if i.get("group_name") == groupName or groupName == None:
                    if tagName == None:
                        return (i.get("group_id"), None)

                    for j in i.get("tag"):
                        if j.get("name") == tagName:
                            return (groupName, j.get("id"))
        return (None, None)

    def add_tag_name(self, groupName, tagName:list=[{'name': int(time.time())}]):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            'method': 'post',
            'params': {'access_token': self.access_token},
            'json': {'group_name': groupName,
                     'tag': tagName}
        }
        r = self.request(data)
        return r

    def edit_tag_name(self, tagNameOld = None, groupNameOld = None, newName = None, newOrder = None):
        if tagNameOld is None and groupNameOld is None:
            return None
        id = self.get_tag_id_by_name(groupName=groupNameOld, tagName=tagNameOld)
        if groupNameOld is not None:
            id = id[0]
        else:
            id = id[1]

        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            'method': 'post',
            'params': {'access_token': self.access_token},
            'json': {'id': id,
                     'name': newName,
                     'order': newOrder}
        }

        r = self.request(data)
        return r

    def del_tag_by_name(self, tagName = None, groupName = None):
        id = self.get_tag_id_by_name(groupName = groupName, tagName = tagName)
        if id == (None, None):
            logger.error("do not find the target tag ID, and del the targer tag failed")
            return None
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            'method': 'post',
            'params': {'access_token': self.access_token},
            'json': {'tag_id': id[1],
                    'group_id': id[0]}
        }
        r = self.request(data)
        return r.json()

    def clear_whole_tag(self):
        r = self.get_whole_tag_list()
        for group in r.json()["tag_group"]:
            self.del_tag_by_name(groupName = group["group_name"])
