from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = "seveniruby"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#curl -XPOST http://127.0.0.1:5000/login?username=dpj&passwd=111
@app.route("/login", methods=['get', 'post'])
def login():
    session['username'] = "session_test"
    res = {
        'url': request.path,
        'methods': request.method,
        'args': request.args,
        'form': request.form,
        'json': request.json,
        'session': session["username"]
    }
    return res

if __name__ == '__main__':
    app.run(debug = True, port = 5000)