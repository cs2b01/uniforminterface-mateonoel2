from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


@app.route('/')
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.users)
    data = users[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')



if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('0.0.0.0'))
