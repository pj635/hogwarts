import requests


class BaseApi():
    def request(self, request: dict):
        if "url" in request:
            return self.http_request(request)
        elif 'rpc' == request.get('protocol'):
            return self.rpc_request(request)

    def http_request(self, request: dict):
        return requests.request(**request)

    def rpc_request(self, request: dict):
        pass