import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def init_sqlite():
    db = get_db()

    with current_app.open_resource('Northwind.sql') as f:
        db.executescript(f.read().decode('latin-1'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_sqlite()
    click.echo('Initialized the database.')


def get_db():
    """
    g is a special object that is unique for each request. It is used to store data that might be accessed by
        multiple functions during the request. The connection is stored and reused instead of creating a new connection
        if get_db is called a second time in the same request.

    current_app: is another special object that points to the Flask application handling the request.
    Since you used an application factory, there is no application object when writing the rest of your code.
    get_db will be called when the application has been created and is handling a request, so current_app can be used.
    """
    print(current_app.config['DATABASE'])
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
