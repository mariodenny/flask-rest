from flask import Flask
from dotenv import load_dotenv
from extensions import db, migrate
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

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

 
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

    with app.app_context():
        print("Registered URLs:")
        for rule in app.url_map.iter_rules():
            print(f"{rule.endpoint} -> {rule.rule}")

    print(f"Registered Blueprints: {app.blueprints}")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
