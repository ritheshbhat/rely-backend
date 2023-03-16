import logging
from os import environ

from werkzeug.exceptions import abort

log = logging.getLogger(__name__)


def load_env_vars(config):
    try:
        config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URL")
        config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        config["SQLALCHEMY_ECHO"] = False
        config["PROPAGATE_EXCEPTIONS"] = True
        config["S3_ENDPOINT"] = environ.get("S3_ENDPOINT")
        config["AWS_ACCESS_KEY"] = environ.get("AWS_ACCESS_KEY")
        config["AWS_SECRET_KEY"] = environ.get("AWS_SECRET_KEY")
        config["RESPONSE_BUCKET_NAME"] = environ.get("RESPONSE_BUCKET_NAME")
        config["S3_REGION"] = environ.get("S3_REGION")
        config["TMP_LOC"] = environ.get("TMP_LOC", "/tmp")
        config['AUTH_PUBLIC_KEY'] = environ.get('AUTH_PUBLIC_KEY')
        config["SERVER_PORT"] = environ.get("SERVER_PORT", 9095)
        config["USE_SYSLOG"] = environ.get("USE_SYSLOG", "True")
        config["DATASET_PATH"] = environ.get("DATASET_PATH","dataset.csv")
        config["REDIS_PORT"] = environ.get("REDIS_PORT")
        config["REDIS_HOST"] = environ.get("REDIS_HOST")
        config["REDIS_PASSWORD"] = environ.get("REDIS_PASSWORD")
        config["DATASET_URL"] = environ.get("DATASET_URL")
        config["DATASET_NAME"] = environ.get("DATASET_NAME")

        return config
    except Exception as e:
        log.debug(f"error while loading env variables {e}")
