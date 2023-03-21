import logging
import logging.config
import logging.handlers
import threading
from flask_cors import CORS

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from src.rely import db, ma

from src.rely.utils.envvars import load_env_vars
from flask_restful import Api

API_ROOT = "/rely/apis"
V1_API_ROOT = "{}/v1".format(API_ROOT)
DATASET_API_ROOT = "{}/dataset".format(V1_API_ROOT)

SEARCH_SUGGESTION_API_ROOT = "{}/suggestion".format(V1_API_ROOT)
app = Flask(__name__)


limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)
def create_app():

    api = Api(app)
    load_env_vars(app.config)

    log = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


    app.app_context().push()
    with app.app_context():
        from src.rely.resources.Dataset import Dataset
        from src.rely.utils.errorhandler import errors
        from src.rely.resources.Health import Health
        from src.rely.resources.Autocomplete import Autocomplete
        from flask_limiter import Limiter
        from flask_limiter.util import get_remote_address
        ma.init_app(app)

        api.add_resource(Health, API_ROOT + "/health")
        api.add_resource(Dataset, DATASET_API_ROOT + "/<string:addr>")
        api.add_resource(Autocomplete,SEARCH_SUGGESTION_API_ROOT +"/<string:address>")
        app.register_blueprint(errors)
        CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://example.com"]}})

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

