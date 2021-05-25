

from flask import Flask, g

import sqlite3



app=Flask(__name__)

app.config['DEBUG']=True
app.config['SECRET_KEY']='kjdkljglkkdfljgkdfjkgj'


def connect_db():
    sql=sqlite3.connect(r'C:\Users\97798\Desktop\flask\traditionaldb\data.db')
    sql.row_factory=sqlite3.Row
    return sql


def get_db():
    if not hasattr(g,'sqlite3'):
        g.sqlite_db=connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
     if  hasattr(g,'sqlite3'):
        g.sqlite_db.close()




@app.route('/')
def home():
    return "<h1>hellow world<h1>"


@app.route('/view')
def view():
    db=get_db()
    cur=db.execute('select id , name , location from users ;')
    result=cur.fetchall()
    return '<h1>the ID {}.The name is {} .. the Location is {}.</h1>'.format(result[1]['id'],result[1]['name'],result[1]['location'])

if __name__ =='__main__':
    app.run(debug=True)