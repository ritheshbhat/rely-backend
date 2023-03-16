import logging
import logging.config
import logging.handlers
import threading

from flask import Flask

from src.rely import db, ma
from src.rely.utils.envvars import load_env_vars
from flask_restful import Api

API_ROOT = "/rely/apis"
V1_API_ROOT = "{}/v1".format(API_ROOT)
DATASET_API_ROOT = "{}/dataset".format(V1_API_ROOT)


def create_app():
    app = Flask(__name__)
    api = Api(app)
    load_env_vars(app.config)

    log = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


    app.app_context().push()
    with app.app_context():
        from src.rely.resources.Dataset import Dataset
        from src.rely.utils.errorhandler import errors
        from src.rely.resources.health import Health
        ma.init_app(app)
        api.add_resource(Health, API_ROOT + "/health")
        api.add_resource(Dataset, DATASET_API_ROOT + "/<string:city>")
        app.register_blueprint(errors)
        log.debug("db initialised...")
        db.init_app(app)
        from src.background_tasks.polling import start_polling
        task_thread = threading.Thread(target=start_polling, args=(app,))
        task_thread.start()
        print(app.url_map)
        log.info(app.url_map)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=app.config["SERVER_PORT"], debug=True)

