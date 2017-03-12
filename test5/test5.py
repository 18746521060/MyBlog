#coding:utf-8
from flask import Flask
import flask
from datetime import datetime
import config
from exts_model import db,Article

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def hello_world():
    # 获取数据库中的数据
    articles = Article.query.order_by(db.desc('create_time')).all()
    # articles = Article.query.order_by('create_time').all()
    return flask.render_template('index.html',articles=articles)

# 写一个过滤器
@app.template_filter('format_time')
def format_time(value):
    # 获取当前时间
    time = datetime.now()
    # 时间差
    rs_time = (time-value).total_seconds()
    # 定义变量
    temp = ''
    if rs_time<60:
        temp = u'刚刚'
    elif rs_time<60*60:
        temp = u'%s分钟前'%int(rs_time/60)
    elif rs_time<60*60*24:
        temp = u'%s小时前'%int(rs_time/(60*60))
    elif rs_time<60*60*24*30:
        temp = u'%s天前'%int(rs_time/(60*60*24))
    elif rs_time<60*60*24*30*12:
        temp = u'%s月前' % int(rs_time / (60 * 60 * 24*30))
    elif rs_time>60*60*24*30*12:
        temp = u'%s年前' % int(rs_time / (60 * 60 * 24 * 30*12))
    return temp

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
