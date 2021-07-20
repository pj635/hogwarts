import json
import sys

import mitmproxy.http
from mitmproxy import http


class Events:
    def recrusion(self, data, multiple = 2):
        if isinstance(data, dict):
            for k, v in data.items():
                data[k] = self.recrusion(v, multiple)

        elif isinstance(data, float):
            data *= multiple

        elif isinstance(data, list):
            data = [self.recrusion(i, multiple) for i in data]

        else:
            data = data
        return data

    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def requestheaders(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def request(self, flow: mitmproxy.http.HTTPFlow):
        headers = [(b'Date', b'Tue, 13 Jul 2021 08:45:52 GMT'), (b'Content-Type', b'application/json; charset=utf-8'),\
                   (b'Transfer-Encoding', b'chunked'), (b'Connection', b'keep-alive'), (b'Server', b'openresty'), \
                   (b'Vary', b'Accept-Encoding'), (b'X-Powered-By', b'Express'), \
                   (b'Cache-Control', b'private, no-store, no-cache, must-revalidate, max-age=0'), (b'X-RT', b'42'), \
                   (b'P3P', b'"CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT""'), \
                   (b'Content-Encoding', b'gzip'), (b'Strict-Transport-Security', b'max-age=31536000')]

        if 'https://xueqiu.com/service/v5/stock/preipo/cn/query' in flow.request.url:
            #实现maplocal
            with open("mapLocal.json", encoding="utf-8", mode='r') as f:
                data = json.load(f)
                data = self.recrusion(data, 2)

                body = json.dumps(data)
                flow.response = http.HTTPResponse.make(200, body, headers)
                print("[DEBUG]%s:%s" % (sys._getframe().f_lineno, flow.response.headers))


    def responseheaders(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if 'https://xueqiu.com/service/v5/stock/chart/minute' in flow.request.url:
            data = json.loads(flow.response.text)
            data["data"]["items"][0]["current"] = 10
            #flow.response.text = json.dumps(data)
            #print("[DEBUG]%s:%s" % (sys._getframe().f_lineno, flow.response.text))

        if 'https://xueqiu.com/service/v5/stock/preipo/cn/query' in flow.request.url:
            a = flow.response.text
            print("[DEBUG]%s:%s" % (sys._getframe().f_lineno, a))

    def error(self, flow: mitmproxy.http.HTTPFlow):
        pass

addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p', '8080', '-s', __file__])

