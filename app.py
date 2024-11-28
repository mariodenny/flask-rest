from datetime import datetime, timedelta
from flask import Flask
from dotenv import load_dotenv
from extensions import db, migrate, jwt
from routes import register_routes
import os
import importlib

load_dotenv()

def create_app():
    app = Flask(__name__)

    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_DATABASE = os.getenv('DB_DATABASE')
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)

    models_dir = os.path.join(os.path.dirname(__file__), 'models')
    if os.path.exists(models_dir):
        for filename in os.listdir(models_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = f"models.{filename[:-3]}"
                try:
                    importlib.import_module(module_name)
                except Exception as e:
                    print(f"Failed to import {module_name}: {e}")

    db.init_app(app)
    migrate.init_app(app, db)

    register_routes(app)

    jwt.init_app(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
