from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

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
    id = db.Column(db.String(20), primary_key = True)
    node_id = db.Column(db.String(20), nullable = False)
    remark = db.remark(db.String(120))

    def __init__(self, id, node_id, remark):
        self.id = id
        self.node_id = node_id
        self.remark = remark

    def __repr__(self):
        return '<Testcase %r>' % self.username



if __name__ == '__main__':
    db.drop_all()
    db.create_all()

