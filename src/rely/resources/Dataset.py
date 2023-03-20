import datetime
import logging
import os
from urllib.parse import unquote

import pandas as pd

from flask import jsonify, current_app, request, make_response
from flask_cors import cross_origin
from flask_restful import Resource
from src.rely.utils.configs import AppConfig

app = current_app._get_current_object()



class Dataset(Resource):
    def get(self, addr: str):
        ac = AppConfig(app)
        decodedPathParam = unquote(addr)
        print("decoded is", decodedPathParam)
        #page_number to avoid chocking of database with ALL data.
        # page_number = int(request.args.get("pno",1))
        # c = city.replace(" ","").lower()
        # response = ac.redis.lrange(c,(int(page_number)*3),int(page_number)*3+6)
        print("inside dataset/", addr)
        response = ac.redis.get(decodedPathParam)

        response_data = {"response": str(response)}
        response = make_response(jsonify(response_data))
        response.headers['Cache-Control'] = 'no-cache'
        response.headers['Last-Modified'] = datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')
        response.headers['Content-Type'] = 'application/json'
        print(":dataset resp", response.json)
        # return the response
        logging.info(response)
        return response
