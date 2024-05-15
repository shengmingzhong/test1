import pymysql
connectiont = pymysql.connect(
    host = 'localhost', # 主机名
    user = 'root',      # 数据库用户名
    password = '',  # 数据库密码
    db = 'hello_database',      # 数据库名
    charset = 'utf8',   # 字符集编码
    cursorclass = pymysql.cursors.DictCursor # 游标类型
)

# 数据列表
# data = [("1",'秒杀'),
#         ("2",'优惠劵'),
#         ("3",'闪购'),
#         ("4",'拍卖'),
#         ("5",'服装城'),
#         ("6",'超市'),
#         ("7",'生鲜'),
#         ]

# data = [("1",'电脑馆'),
#         ("2",'游戏极品'),
#         ("3",'装机大师'),
#         ("4",'职场焕新'),
#         ("5",'虚拟现实'),
#         ("6",'二合一平板'),
#         ("7","电子教育")
#         ]

# data = [("1",'【赠小风扇】维他 柠檬茶250ml*32盒 礼品装 整箱','71.9','89.6','/static/img/seckill-item1.jpg'),
#         ("2",'Kindle Paperwhite 全新升级版6英寸护眼非反光电子墨水','989.0','1299.0','/static/img/seckill-item2.jpg'),
#         ("3",'粮悦 大吃兄糯米锅巴 安徽特产锅巴糯米原味400g*2盒','21.8','49.0','/static/img/seckill-item3.jpg'),
#         ("4",'【京东超市】清风（APP）抽纸 原木纯品金装系列 3层','49.9','109.0','/static/img/seckill-item4.jpg'),
#         ("5",'NIKE耐克 男子休闲鞋 AIR MAX 90 ESSENTIAL 气垫','559','798.0','/static/img/seckill-item1.jpg'),
#
#         ]

# data = [("1",'休闲零食'),
#         ("2",'坚果'),
#         ("3",'牛奶'),
#         ("4",'饮料冲调'),
#         ("5",'食用油'),
#         ("6",'大米'),
#         ("7","酒类"),
#         ("8","烧烤食材")
#         ]

# data = [("1",'电脑馆','笔记本999元限量秒！','/static/img/item-computer-2.jpg'),
#         ("2",'外设装备','1000减618','/static/img/item-computer-1-3.jpg'),
#         ("3",'电脑配件','联合满减<br>最高省618','/static/img/item-computer-1-4.jpg'),
#         ("4",'办公生活','5折神券 精品文具','/static/img/item-computer-1-5.jpg')
#         ]
#
# data = [("1",'平板电脑','爆款平板12期免息','/static/img/item-computer-2-2.jpg'),
#         ("2",'智能酷玩','抢999减666神券','/static/img/item-computer-2-3.jpg'),
#         ("3",'娱乐影音','大牌耳机低至5折','/static/img/item-computer-2-4.jpg'),
#         ("4",'摄影摄像','大牌相机5折抢','/static/img/item-computer-2-5.jpg')
#         ]

# data = [("1",'粮油调味','买2免1','/static/img/item-eat-1-2.jpg'),
#         ("2",'饮料冲调','第二件半价','/static/img/item-eat-1-3.jpg'),
#         ("3",'休闲零食','满99减40','//static/img/item-eat-1-4.jpg'),
#         ("4",'中外名酒','满199减100','/static/img/item-eat-1-5.jpg')
#         ]

# data = [("1",'东家菜','丰富好味','/static/img/item-eat-2-2.jpg'),
#         ("2",'东家菜','丰富好味','/static/img/item-eat-2-2.jpg'),
#         ("3",'东家菜','丰富好味','/static/img/item-eat-2-2.jpg'),
#         ("4",'东家菜','丰富好味','/static/img/item-eat-2-2.jpg')
#         ]


# data = [("1",'/static/img/item-computer-1.jpg'),
#         ("2",'/static/img/item-computer-1-6.jpg'),
#         ("3",'/static/img/item-computer-1-7.jpg'),
#         ("4",'/static/img/item-computer-1-8.jpg'),
#         ("5",'/static/img/item-computer-2-1.jpg'),
#         ("6",'/static/img/item-computer-2-6.jpg'),
#         ("7",'/static/img/item-computer-2-7.jpg'),
#         ("8",'/static/img/item-computer-2-8.jpg'),
#         ("9", '/static/img/item-eat-1-1.jpg'),
#         ("10", '/static/img/item-eat-1-6.jpg'),
#         ("11", '/static/img/item-eat-1-7.jpg'),
#         ("12", '/static/img/item-eat-1-8.jpg'),
#         ("13", '/static/img/item-eat-2-1.jpg'),
#         ("14", '/static/img/item-eat-2-6.jpg'),
#         ("15", '/static/img/item-eat-2-7.jpg'),
#         ("16", '/static/img/item-eat-2-8.jpg'),
#         ]
cursor = connectiont.cursor() # 获取游标对象
try:
    # 执行sql语句，插入多条数据
    # cursor.executemany("insert into category_temp(id, cname) values (%s,%s)", data)
    # cursor.executemany("insert into computer_temp(id, cname) values (%s,%s)", data)
    # cursor.executemany("insert into product(id, pname,new_price,old_price,images) values (%s,%s,%s,%s,%s)", data)
    # cursor.executemany("insert into eat_temp(id, cname) values (%s,%s)", data)
    # cursor.executemany("insert into computer1(id, pname,introduce,images) values (%s,%s,%s,%s)", data)
    # cursor.executemany("insert into eat2(id, pname,introduce,images) values (%s,%s,%s,%s)", data)
    # cursor.executemany("insert into blend(id,images) values (%s,%s)", data)
    # 提交数据
    connectiont.commit()
except:
    # 发生错误时回滚
    print("发生错误时回滚")
    connectiont.rollback()

print("ok")
connectiont.commit()
cursor.close()      # 关闭游标
connectiont.close() # 关闭连接