from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/h_sy')
def h_sy():
    return render_template("index.html")
@app.route('/feedback')
def feedback():
    return render_template("feedback.html")


#
# @app.route('/')
# def feedback():
#     return render_template("signup.html")

def insert_data(username, password, email,city):
    import pymysql
    connectiont = pymysql.connect(
        host='localhost',  # 主机名
        user='root',  # 数据库用户名
        password='',  # 数据库密码
        db='hello_database',  # 数据库名
        charset='utf8',  # 字符集编码
        cursorclass=pymysql.cursors.DictCursor  # 游标类型
    )
    # 数据列表
    data = [(username, password, email, city)]
    print(data)
    cursor = connectiont.cursor()  # 获取游标对象
    try:
        # 执行sql语句，插入多条数据
        cursor.executemany("insert into user_table(username, password, email, city) values (%s,%s,%s,%s)", data)
        # 提交数据
        connectiont.commit()
    except:
        # 发生错误时回滚
        connectiont.rollback()
    connectiont.commit()
    cursor.close()  # 关闭游标
    connectiont.close()  # 关闭连接

@app.route('/register', methods=['GET','POST'])
def register():

    if (request.method == "POST"):
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        city = request.form['city']

        print(username)
        print(password)
        print(email)
        print(city)

        insert_data(username, password, email,city)
        return render_template("index.html")
        # return redirect("/")

    else: #GET
         return render_template("signup.html")

if __name__ == '__main__':
    app.run()