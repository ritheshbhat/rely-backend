import logging
from urllib.parse import unquote

from flask import current_app
from flask_restful import Resource

from src.rely.cache.redis import CacheManager
from src.rely.utils.configs import AppConfig
from src.rely.utils.utils import add_response_headers

app = current_app._get_current_object()



class Autocomplete(Resource):
    def get(self, address: str):
        address = unquote(address)
        cache = CacheManager(1, AppConfig(app))
        suggestions = cache.get_suggestions_for_key_strokes(address)
        response_data = {"response": suggestions}
        response = add_response_headers(response_data)
        logging.info(response)
        return response
