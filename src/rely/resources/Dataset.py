import datetime
import json
import logging
import os
from urllib.parse import unquote

import pandas as pd

from flask import jsonify, current_app, request, make_response
from flask_cors import cross_origin
from flask_restful import Resource

from src.rely.cache.redis import CacheManager
from src.rely.utils.configs import AppConfig
from src.rely.utils.utils import add_response_headers

app = current_app._get_current_object()


class Dataset(Resource):
    def get(self, addr: str):
        address = unquote(addr)
        page_number = int(request.args.get("page"))
        cache = CacheManager(page_number, AppConfig(app))
        properties = []
        property = json.loads(cache.get_properties_for_given_address(address).decode())
        properties.append(property)
        zip = property[2]
        start_index = (page_number - 1) * 2
        end_index = start_index + 2
        nearby_properties = cache.get_nearby_properties_from_zip(zip, start_index, end_index)
        logging.info("nearby properties are"+str(nearby_properties))
        for i in nearby_properties:
            properties.append(json.loads(cache.get_properties_for_given_address(i).decode()))
        response_data = {"response": str(properties)}
        response = add_response_headers(response_data)
        logging.info(response.json)
        return response
