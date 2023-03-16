import logging

import redis

log = logging.getLogger(__name__)

class AppConfig:

    def __init__(self, app):
        self.dataset_url = app.config["DATASET_URL"]
        self.dataset = app.config["DATASET_NAME"]
        self.aws_secret_key = app.config["AWS_SECRET_KEY"]
        self.aws_access_key = app.config["AWS_ACCESS_KEY"]
        self.s3_region = app.config["S3_REGION"]
        self.s3_endpoint = app.config["S3_ENDPOINT"]
        self.tmp_loc = app.config["TMP_LOC"]
        self.redis = redis.Redis(host=app.config["REDIS_HOST"], port=app.config["REDIS_PORT"], password=app.config["REDIS_PASSWORD"])

class UserContext:
    def __init__(self, claims):
        log.debug(f"Building user context from {claims}")
        self.user_id = claims["uid"]
        self.mobile = claims.get("mob", None)
        self.email = claims.get("eml", None)

