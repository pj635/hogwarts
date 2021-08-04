import requests

class Testcase:
    url = "http://127.0.0.1:5000"

    def test_get(self):
        responce = requests.get(self.url, params = {"id": 1})
        print()
        print(type(responce.json()))
        print(responce.json())
        print(responce.text)
        print(responce.status_code)

    def test_post(self):
        # data = {"id": 1, "node_id": "1", "remark": "testcase1"}
        # responce = requests.post(self.url, json = data)
        # print(responce.status_code)

        data = {"id": 1, "node_id": 1, "remark": "testcase1"}
        responce = requests.post(self.url, json=data)
        data = {"id": 2, "node_id": 2, "remark": "testcase1"}
        responce = requests.post(self.url, json=data)
        data = {"id": 3, "node_id": 3, "remark": "testcase1"}
        responce = requests.post(self.url, json=data)
        data = {"id": 4, "node_id": 4, "remark": "testcase1"}
        responce = requests.post(self.url, json=data)
        data = {"id": 5, "node_id": 5, "remark": "testcase1"}
        responce = requests.post(self.url, json=data)
        data = {"id": 6, "node_id": 6, "remark": "testcase1"}
        responce = requests.post(self.url, json=data)
        data = {"id": 7, "node_id": 7, "remark": "testcase1"}
        responce = requests.post(self.url, json=data)
        data = {"id": 8, "node_id": 8, "remark": "testcase1"}
        responce = requests.post(self.url, json=data)

    def test_post2(self):
        data = {"id": 10, "node_id": ['1', '2'], "remark": "testcase1"}
        responce = requests.post(self.url, json = data)
        print(responce.status_code)

    def test_put(self):
        fix_data = {"id": 1, "node_id": "1_bak", "remark": "testcase1_bak"}
        responce = requests.put(self.url, json = fix_data)
        print(responce)

    def test_delete(self):
        responce = requests.delete(url = self.url)
        assert responce.json().get("error") == 40001

        responce = requests.delete(url = self.url, params = {"id": 1})
        assert responce.json().get("error") == 0