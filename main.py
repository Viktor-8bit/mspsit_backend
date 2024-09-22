import json

from sqlalchemy import *
from sqlalchemy.orm import *
from flask import Flask, request

from datetime import datetime
from bd_model import log, comment, Base



engine = create_engine("sqlite:///DataBase.db")
session = Session(engine)
Base.metadata.create_all(engine)


app = Flask(__name__)


# добавить коментарий к логу 
@app.route("/api/add_comment_to_log/<int:log_id>")
def add_comment_to_log(log_id):
    return ''

# добавить лог записб 
@app.route("/api/add_log", methods=['POST'])
def add_log():
    data = request.json
    try:
        temp_log = log(ip=data["ip"], data=datetime.strptime(data["data"], '%Y-%m-%d %H:%M:%S'), status=data["status"], query=data["query"], user_agent=data["user_agent"])
        session.add(temp_log)
        session.commit()
        return "Ok"
    except Exception:
        print(Exception.with_traceback())
        return "Failed"

    
# получить все логи
@app.route("/api/get_all_logs")
def get_all_logs():
    query = session.query(log)
    logs = query.all()
    return json.dumps([log.to_dict() for log in logs])

# получить конкретный лог 
@app.route("/api/get_log_buId/<int:log_id>")
def get_log_buId(log_id):
    query = session.query(log).filter(log.id == log_id).first()
    return json.dumps(query.to_dict())

# удалить лог ???

