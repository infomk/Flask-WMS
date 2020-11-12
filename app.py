

import flask
from flask_cors import CORS
import yaml

# Read config file
with open('config/config.yaml') as config_file:
    config = yaml.load(config_file, Loader=yaml.FullLoader)
    config = config['FlaskWms']

app = flask.Flask(__name__)
app.config["DEBUG"] = config['config']['debug']

# Register blueprint Routes
from modules.wms import *
app.register_blueprint(routes)


# Enable CORS
cors = CORS(app, resources={r"/wms/*": {"origins": "*"}})


# Run app
if __name__ == '__main__':
    app.run('0.0.0.0', config['config']['port'])
