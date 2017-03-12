#coding:utf-8

from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager,Server
from test5 import app
from exts_model import db,Article
from datetime import datetime

app.config.from_pyfile('config.py')
db.init_app(app)
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
manager.add_command('runserver',Server)

@manager.option('-t',dest='title')
@manager.option('-c',dest='content')
def add_article(title,content,create_time=datetime.now()):
    article = Article(title=title,content=content,create_time=create_time)
    db.session.add(article)
    db.session.commit()
    print 'success'
    return 'success'


if __name__=='__main__':
    manager.run()