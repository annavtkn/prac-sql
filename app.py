from flask import Flask, render_template, g, request
import sqlite3

app = Flask(__name__)

DATABASE = "./database.db"

users_columns=('id', 'login', 'money_amount', 'card_number', 'status')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_conn(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=()):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return rv


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users')
def get_users():
    active_users = query_db("select id, login from users where status=1")
    return render_template("users.html", header="Active users: ", users=active_users, columns=users_columns[:2])


@app.route('/by-id', methods=['GET'])
def user_by_id(user_id=None):
    if not user_id:
        user_id = request.args['id']
    users = query_db(f"select * from users where id={user_id}")
    return render_template("users.html", header="User: ", users=users, columns=users_columns)


@app.route('/by-login', methods=['GET'])
def user_by_login():
    query = f"select * from users where login={request.args['login']}"
    print(query)
    users = query_db(f"select * from users where login='{request.args['login']}'")
    return render_template("users.html", header="User: ", users=users, columns=users_columns)


if __name__ == '__main__':
    pass
