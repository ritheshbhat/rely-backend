import os

import pandas as pd

from flask import jsonify, current_app, request, make_response
from flask_restful import Resource
from src.rely.utils.configs import AppConfig

app = current_app._get_current_object()


class Dataset(Resource):
    def get(self, city:str):
        ac = AppConfig(app)
        #page_number to avoid chocking of database with ALL data.
        page_number = int(request.args.get("pno",1))
        c = city.replace(" ","").lower()
        response = ac.redis.lrange(c,(int(page_number)*3),int(page_number)*3+6)
        print(response)


        return jsonify({'response': str(response)})