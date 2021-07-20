import json

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

username = "root"
pwd = "root"
ip = "127.0.0.1"
port = "3306"
database = "hogwarts"
# 设置mysql 链接方法是
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
# 解决warning问题
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Testcase(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    node_id = db.Column(db.String(20), nullable = False)
    remark = db.Column(db.String(120))

    def __init__(self, id, node_id, remark):
        self.id = id
        self.node_id = json.dumps(node_id)
        self.remark = json.dumps(remark)

    def __repr__(self):
        return '<Testcase %s:%s>:%s' % (self.id, self.node_id, self.remark)

class Service(Resource):
    def get(self):
        filter_id = request.args.get("id")
        app.logger.info("filter_id:%s", filter_id)
        if filter_id is not None:
            data = Testcase.query.filter_by(id = filter_id).first()
            app.logger.info("query data:%s", data)
            responce = [(data.id, data.node_id, data.remark)]
            app.logger.info(responce)
        else:
            data = Testcase.query.all()
            responce = [(i.id, i.node_id, i.remark) for i in data]
            app.logger.info(responce)
        return {"error": 0, "msg": {"data": responce}}

    def post(self):
        data = request.json
        app.logger.info(data)
        testcase = Testcase(**data)
        db.session.add(testcase)
        db.session.commit()
        return {"error": 0, "msg": "post a testcase info success"}

    def put(self):
        data = request.json
        app.logger.info(data)
        filter_id = data.get("id")
        Testcase.query.filter_by(id = filter_id).update(data)
        db.session.commit()
        return {"error": 0, "msg": "update a testcase info success"}

    def delete(self):
        filter_id = request.args.get("id")
        if filter_id is None:
            return {"error": 40001, "msg": "delete a testcase info failed and the value of id is None"}
        Testcase.query.filter_by(id = filter_id).delete()
        db.session.commit()
        return {"error": 0, "msg": "delete a testcase info success"}

api.add_resource(Service, '/')

if __name__ == '__main__':
    #db.drop_all()
    db.create_all()
    app.run(debug=True, port = 5000)