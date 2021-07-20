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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, id, username, email):
        self.username = username
        self.email = email
        self.id = id

    def __repr__(self):
        return '<User %r>' % self.username



if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    user1 = User(1, "张三", "2559394890@qq.com")
    db.session.add(user1)
    user2 = User(2, "张四", "2559394891@qq.com")
    user3 = User(3, "张五", "2559394892@qq.com")
    user4 = User(4, "张六", "2559394893@qq.com")
    user5 = User(5, "张七", "2559394894@qq.com")
    db.session.add_all([user2, user3, user4, user5])
    db.session.commit()

    print(User.query.all())
    res = User.query.filter_by(id = 1).first()
    print(res.id)
    res = User.query.filter_by(id = 2).delete()
    db.session.commit()
    res = User.query.filter_by(id = 3).update({"email": "99@.com"})
    db.session.commit()