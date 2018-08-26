from flask import Flask, render_template, request
from controller import users_controller


app = Flask(__name__)
app.config.from_pyfile('./config.cfg')


# ================ home ======================
@app.route('/', methods=["GET", "POST"])
def show():
    return render_template('index.html')


# ========== login =============================
@app.route('/login', methods=["GET", "POST"])
def login():
    result = users_controller.do_login(request)
    return result


# ========================= User Controller ==================================
# ------------------------- create user --------------------------------------
@app.route('/user/create', methods=["GET", "POST"])
def create_user():
    return users_controller.create_user(request)


# --------------------------------show all information user---------------------
@app.route('/user', methods=["GET", "POST"])
def show_all_info_user():
    return users_controller.show_all_info_user(request)


# ------------------------- detail user --------------------------------------

@app.route('/user/info', methods=["GET", "POST"])
def get_user():
    return users_controller.get_user(request)


@app.route('/user/delete', methods=["GET", "POST"])
def delete_user():
    return users_controller.delete_user(request)


@app.route('/user/edit', methods=["GET", "POST"])
def edit_user():
    return users_controller.edit_user(request)

