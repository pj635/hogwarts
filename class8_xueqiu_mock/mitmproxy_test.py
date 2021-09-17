import json
import sys

import mitmproxy.http
from mitmproxy import http


class Events:
    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def requestheaders(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def request(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def responseheaders(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):

        if 'https://xueqiu.com/service/v5/stock/preipo/cn/query' in flow.request.url:
            # 实现maplocal
            with open("mapLocal.json", encoding="utf-8", mode='r') as f:
                body = f.read()

                headers = flow.response.headers
                flow.response = http.HTTPResponse.make(200, body, headers)

        if 'https://xueqiu.com/service/v5/stock/preipo/cn/query' in flow.request.url:
            #实现rewrite
            data = json.loads(flow.response.text)
            data['data']['items'][1]['name'] = 'dpj1'
            data['data']['items'][2]['name'] = 'dpj2'
            data['data']['items'][1]['actissqty'] = 9999999999999999
            data['data']['items'][2]['actissqty'] = 9999999999999999
            flow.response.text = json.dumps(data)



    def error(self, flow: mitmproxy.http.HTTPFlow):
        pass

addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p', '8880', '-s', __file__])

