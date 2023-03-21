from datetime import datetime

from flask import make_response, jsonify


def add_response_headers(response):

    response_with_headers = make_response(jsonify(response))
    response_with_headers.headers['Cache-Control'] = 'no-cache'
    response_with_headers.headers['Last-Modified'] = datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')
    response_with_headers.headers['Content-Type'] = 'application/json'
    return response_with_headers