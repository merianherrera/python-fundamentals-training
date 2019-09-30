import os

from flask import Flask, jsonify, render_template
from db_sample.db import init_db, db_session
from db_sample.import_db import init_app
from db_sample.models import Category, Customers


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'sqlite:///northwind.db'),
    )

    # init SQLAlchemy
    init_db()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    @app.route('/categories')
    def list_categories():
        categories = db_session.query(Category).all()
        return jsonify([{'name': cat.CategoryName, 'desc': cat.Description} for cat in categories]), \
               {'Content-Type': 'application/json; charset=utf-8'}

    @app.route('/render-clients')
    def render_clients():
        customers = db_session.query(Customers).all()
        return render_template('render_sample.html', customers=customers)

    return app


