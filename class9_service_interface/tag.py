import time

import requests


class Tag():
    def __init__(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        corpid = 'ww56b541eb0eab2661'
        corpsecret = 'i8lbbMoby8YP1nJoDJuhT8Xc52-PRfB-vrjSTDcs1YM'
        r = requests.get(url, params={'corpid': corpid,
                                      'corpsecret': corpsecret})
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        self._access_token = r.json()["access_token"]

    def get_whole_tag_list(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list'
        r = requests.post(url, params = {'access_token': self._access_token})
        #print(json.dumps(r.json(), indent=2, ensure_ascii=False))
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

    def add_tag_name(self, groupName, tagName:list=[int(time.time())]):
        tag = []
        for i in tagName:
            tag.append({"name": str(i)})
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        r = requests.post(url,
                          params={'access_token': self._access_token},
                          json={'group_name': groupName,
                                'tag': tag}
                          )
        return r

    def edit_tag_name(self, tagNameOld = None, groupNameOld = None, newName = None, newOrder = None):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag'
        if tagNameOld is None and groupNameOld is None:
            return None
        id = self.get_tag_id_by_name(groupName=groupNameOld, tagName=tagNameOld)
        if groupNameOld is not None:
            id = id[0]
        else:
            id = id[1]

        r = requests.post(url,
                          params = {'access_token': self._access_token},
                          json={'id': id,
                            'name': newName,
                            'order': newOrder}
                          )
        return r

    def del_tag_by_name(self, tagName = None, groupName = None):
        id = self.get_tag_id_by_name(groupName = groupName, tagName = tagName)
        print("*" * 100)
        print("id:%s" % (id,))
        if id == (None, None):
            print("do not find the target tag ID, and del the targer tag failed")
            return None
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag'
        r = requests.post(url,
                          params = {'access_token': self._access_token},
                          json={'tag_id': id[1],
                                'group_id': id[0]}
                          )
        print(r.json())
        return r.json()

    def clear_whole_tag(self):
        r = self.get_whole_tag_list()
        for group in r.json()["tag_group"]:
            self.del_tag_by_name(groupName = group["group_name"])