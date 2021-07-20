from hogwarts_homework.homework7_server_apiObject.base_api import BaseApi

class Wework(BaseApi):
    def __init__(self, secret):
        corpid = 'ww56b541eb0eab2661'
        # corpsecret = 'i8lbbMoby8YP1nJoDJuhT8Xc52-PRfB-vrjSTDcs1YM'
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "method": "get",
            "params": {
                'corpid': corpid,
                'corpsecret': secret
            }
        }
        r = self.request(data)
        self.access_token = r.json()["access_token"]