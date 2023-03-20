import datetime
import logging
import os

import pandas as pd

from flask import jsonify, current_app, request, make_response
from flask_cors import cross_origin
from flask_restful import Resource
from src.rely.utils.configs import AppConfig

app = current_app._get_current_object()



class Autocomplete(Resource):
    def get(self, address: str):
        prefix = address
        ac = AppConfig(app)
        count = 8
        results = []
        grab = 50
        start = ac.redis.zrank('autocomplete', prefix)
        if not start:
            return []
        while (len(results) != count):
            rang = ac.redis.zrange('autocomplete', start, start + grab - 1)
            start += grab
            if not rang or len(rang) == 0:
                break
            range = [addr.decode() for addr in rang]
            for entry in range:

                minlen = min(len(entry), len(prefix))

                if entry[0:minlen] != prefix[0:minlen]:
                    count = len(results)
                    break
                if entry[-1] == "%" and len(results) != count:
                    results.append(entry[0:-1])

        print("res", results)
        response_data = {"response": results}
        response = make_response(jsonify(response_data))
        response.headers['Cache-Control'] = 'no-cache'
        response.headers['Last-Modified'] = datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')

        response.headers['Content-Type'] = 'application/json'
        logging.info(response)
        return response
