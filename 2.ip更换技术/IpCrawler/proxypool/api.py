# -*- coding: utf-8 -*-

import flask
import json
from db.mongo_db import MongoDB
import random

app = flask.Flask(__name__)

@app.route('/one')
def get_one():
    proxies = MongoDB().get(1)
    result = [proxy['proxy'] for proxy in proxies]
    x = random.randint(0, MongoDB().get_count() - 1)
    return json.dumps(dict(proxy=result[x]))

@app.route('/all')
def get_many():
    proxies = MongoDB().get(1)
    result = [proxy['proxy'] for proxy in proxies]
    print(result)
    print(MongoDB().get_count())
    return json.dumps(result)


@app.route('/delete')
def delete():
    args = flask.request.args
    MongoDB().delete({'proxy': args['proxy']})
    return '删除成功：{}'.format(args)


def run():
    app.run()



