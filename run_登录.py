from flask import Flask,render_template, request,redirect,url_for,session,jsonify
from mysql_util import MysqlUtil
import random
import os
app = Flask(__name__)
app.secret_key = 'mrsoft12345678' # 设置秘钥

@app.route('/')
def index():
    db = MysqlUtil()
    sql = 'SELECT * FROM category_temp'
    categorys = db.fetchall(sql)  # 获取多条记录

    db = MysqlUtil()
    sql1 = 'SELECT * FROM computer_temp'
    computers = db.fetchall(sql1)


    db = MysqlUtil()
    sql2 = 'SELECT * FROM product'
    products1 = db.fetchall(sql2)

    db = MysqlUtil()
    sql3 = 'SELECT * FROM eat_temp'
    eats = db.fetchall(sql3)

    db = MysqlUtil()
    sql4 = 'SELECT * FROM computer1'
    computers1 = db.fetchall(sql4)

    db = MysqlUtil()
    sql5 = 'SELECT * FROM computer2'
    computers2 = db.fetchall(sql5)

    db = MysqlUtil()
    sql6 = 'SELECT * FROM eat1'
    eats1 = db.fetchall(sql6)

    db = MysqlUtil()
    sql7 = 'SELECT * FROM eat2'
    eats2 = db.fetchall(sql7)

    db = MysqlUtil()
    sql8 = 'SELECT * FROM blend where id=1'
    blends1 = db.fetchall(sql8)

    db = MysqlUtil()
    sql9 = 'SELECT * FROM blend where id>1 and id<5'
    blends2 = db.fetchall(sql9)

    db = MysqlUtil()
    sql10 = 'SELECT * FROM blend where id>5 and id<9'
    blends3 = db.fetchall(sql10)

    db = MysqlUtil()
    sql11 = 'SELECT * FROM blend where id=9'
    blends4 = db.fetchall(sql11)

    db = MysqlUtil()
    sql12 = 'SELECT * FROM blend where id>9 and id<13'
    blends5 = db.fetchall(sql12)

    db = MysqlUtil()
    sql13 = 'SELECT * FROM blend where id>13 and id<=16'
    blends6 = db.fetchall(sql13)

    db = MysqlUtil()
    sql14 = 'SELECT * FROM blend where id=17'
    blends7 = db.fetchall(sql14)

    db = MysqlUtil()
    sql15 = 'SELECT * FROM blend where id=18'
    blends8 = db.fetchall(sql15)

    return render_template("index.html", categorys=categorys,computers=computers,products1=products1,eats=eats,computers1=computers1,
                           computers2=computers2,eats1=eats1,eats2=eats2,blends1=blends1,blends2=blends2,blends3=blends3,blends4=blends4,
                           blends5=blends5,blends6=blends6,blends7=blends7,blends8=blends8)
    # return render_template("index.html")

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/h_sy')
def h_sy():
    return redirect(url_for('index'))

@app.route('/feedback')
def feedback():
    return render_template("feedback.html")

@app.route('/product_echars')
def product_echars():
    return render_template("product_echars.html")

@app.route('/get_company', methods=['GET'])
def get_company():

    json = request.json
    print('recv:', json)
    db = MysqlUtil()
    sqla = 'SELECT COUNT(*) FROM category_temp'
    result1 = db.fetchall(sqla)
    count1 = result1[0]['COUNT(*)']  # 提取列表中的第一个字典，并访问'COUNT(*)'键
    print(count1)  # 输出数字


    db = MysqlUtil()
    sqlb = 'SELECT COUNT(*) FROM product'
    result2 = db.fetchall(sqlb)  # 注意：这里我假设您的 MysqlUtil 类有一个 execute_query 方法
    count2 = result2[0]['COUNT(*)']   # 假设 execute_query 返回的是一个结果集，我们需要第一个结果（即 COUNT(*) 的值）

    db = MysqlUtil()
    sqlc = 'SELECT SUM(new_price) FROM product '
    result3 = db.fetchall(sqlc)  # 注意：这里我假设您的 MysqlUtil 类有一个 execute_query 方法
    print(result3)
    count3 = result3[0]['SUM(new_price)']   # 假设 execute_query 返回的是一个结果集，我们需要第一个结果（即 COUNT(*) 的值）
    price=count3/count2


    re_data = {
           'company_num': count1,
           'job_num': count2,
           'avg_salary': price,
    }
    # json = request.json
    # print('recv:', json)
    # re_data = {
    #        'company_num': 1001,
    #        'job_num': 5001,
    #        'avg_salary': 50001,
    # }
    return jsonify(re_data)

@app.route('/bashboard')
def bashboard():
    db = MysqlUtil()
    sql = 'SELECT * FROM product'
    products = db.fetchall(sql)  # 获取多条记录
    print(products)

    return render_template("product_board.html",products=products)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'jpg', 'png','jpeg',"bmp"}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/add_product',methods=['GET','POST'])
def add_product():
    db = MysqlUtil()
    sql = 'SELECT * FROM category_temp'
    categorys = db.fetchall(sql)  # 获取多条记录
    if (request.method == "POST"):
        pname = request.form.get("pname")
        pDesc = request.form.get("pDesc")
        counts = request.form.get("counts")
        old_price = request.form.get("old_price")
        new_price = request.form.get("new_price")
        print(pname)
        print(pDesc)
        print(counts)
        print(old_price)
        print(new_price)

        file = request.files['file']
        if file.filename == '':
            return '没有选择文件', 400
        if file and allowed_file(file.filename):
            filename = file.filename
            file_name, file_ext = os.path.splitext(os.path.basename(filename))
            # print(file_name)
            print(file_ext)
            dir_name = "./static/img/me/"
            new_name = str(random.randint(1,10000)) + file_ext
            print(dir_name)
            images_path = os.path.join(dir_name, new_name)
            print(images_path)
            file.save(images_path)

        id = "%d" % random.randint(0,1000000000)
        # images_path = "/static/product_test/2.jpg"
        db = MysqlUtil() # 实例化数据库操作类
        sql = "INSERT INTO product(id,pname,old_price,new_price,counts,images) \
               VALUES ('%s', '%s', '%s','%s','%s','%s')" % (id,pname,old_price,new_price,counts,images_path) # 插入数据的SQL语句
        db.insert(sql)
        return redirect(url_for('bashboard'))
    else:
        return render_template("add_product.html", categorys=categorys)

@app.route('/delete_product/<string:id>', methods=['POST'])
def delete_product(id):
    db = MysqlUtil()
    sql = "DELETE FROM product WHERE id='%s'" % (id)
    db.delete(sql)
    return redirect(url_for('bashboard'))

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

        db = MysqlUtil()
        sql = "INSERT INTO user_table(username,password,email,city) \
        VALUES ('%s', '%s', '%s','%s')" % (username,password,email,city) # 插入数据的SQL语句

        product_list = db.insert(sql)  # 获取多条记录

        print(product_list)

        # insert_data(username, password, email)
        # return render_template("index.html")
        return redirect(url_for('index'))


    else: #GET
         return render_template("signup.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if (request.method == "POST"):
        print("ok")
        username = request.form['username']
        password_candidate = request.form['password']
        print(username)
        sql = "SELECT * FROM user_table  WHERE username = '%s'" % (username)  # 根据用户名查找user表中记录
        db = MysqlUtil()  # 实例化数据库操作类
        result = db.fetchone(sql)  # 获取一条记录
        print(password_candidate)
        print(result)
        db_password = result['password']  # 用户填写的密码
        if password_candidate == db_password:
            # 写入session
            session['logged_in'] = True
            session['username'] = username

            # return "登录成功"# 跳转到控制台
            return redirect(url_for('index'))
        else:
            print("密码错误")
            return render_template("login.html")

    else: #GET
         return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear() # 清除Session
    return redirect(url_for('index'))

app.run(debug=True)