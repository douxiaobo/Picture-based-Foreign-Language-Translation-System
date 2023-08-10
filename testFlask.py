from flask import Flask, request, render_template,jsonify,redirect

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, !</p>"

# @app.route("/blog/list")
# def blog_list():
#     return "博客列表"

# # 带参数，把参数固定在了path
# @app.route("/blog/<int:blog_id>") # 参数类型int
# def blog_detail(blog_id):
#     return "博客是：%s" % blog_id

# # 查询字符串的方式传参
# @app.route('/book/list')
# def book_list():
#     # arguments 参数  request.arg类字典类型
#     page = request.args.get("page", default = 1, type = int)
#     return f"页码是{page}"
# # http://127.0.0.1:5000/book/list 默认返回第一页
# # http://127.0.0.1:5000/book/list?page=2 
 



# jinja2

# @app.route("/")
# def hello_world():
#     return render_template("index.html")

@app.route("/blog/<blog_id>")
def blog_detail(blog_id):
    return render_template("blog_detail.html", blog_id = blog_id, username = "马") # 传参数过去


class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

@app.route('/')
def hello():
    user = User(username="ma", email="163@com")
    person = {
        "username":"ma",
        "email":"qq.com"

    }
    return render_template("index2.html",user = user,person = person)



# # get 前面写了post不支持
# @app.route('/login', methods=['GET', 'POST'])
# def login():  # 默认情况这个函数只能接收get请求

#     return render_template('login.html')
# # return render_template(xx.html)
# # return jsonify({'code':1000, 'data':[1,2,3]})

@app.route('/login', methods=['GET', 'POST'])
def login():  # 默认情况这个函数只能接收get请求
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'ma' and pwd == 'ma':
        return redirect('/index')# 跳转    return "登录成功" 
    # return "用户名或密码错误"
    error = '用户名或密码错误'
    return render_template('login.html',error=error) # **{'error':error}

@app.route('/index')
def index():
    return '首页'




if __name__ == '__main__':
    app.run(debug = True) 
