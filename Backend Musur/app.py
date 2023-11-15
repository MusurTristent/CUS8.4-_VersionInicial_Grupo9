from flask import Flask
from routes.persona_routes import persona_routes
from routes.casa_infraccion_routes import casa_infraccion_routes
from routes.casa_routes import casa_routes
from routes.infraccion_routes import infraccion_routes
from routes.propietario_routes import propietario_routes
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
from flask_cors import CORS
from utils.db import db

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = 'clavesecreta123'

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db.init_app(app)

app.register_blueprint(persona_routes)
app.register_blueprint(casa_infraccion_routes)
app.register_blueprint(casa_routes)
app.register_blueprint(infraccion_routes)
app.register_blueprint(propietario_routes)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
