
from sqlalchemy import *
from sqlalchemy.orm import *

from model import *

from flask import Flask



engine = create_engine("sqlite:///DataBase.db")
session = Session(engine)


app = Flask(__name__)


# добавить коментарий к логу 
@app.route("/api/add_comment_to_log/<int:log_id>")
def add_comment_to_log(log_id):
    return ''

# добавить лог записб 
@app.route("/api/add_log")
def add_log():
    return ''

# получить все логи
@app.route("/api/get_all_logs")
def get_all_logs():
    return ''

# получить конкретный лог 
@app.route("/api/get_log_buId/<int:log_id>")
def get_log_buId(log_id):
    return ''

# удалить лог ???

