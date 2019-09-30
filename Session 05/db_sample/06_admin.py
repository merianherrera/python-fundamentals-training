from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from db_sample.db import init_db, db_session
from db_sample.models import Customers, Category

app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
init_db()
admin = Admin(app, name='Sample North Wind', template_mode='bootstrap3')
# Add administrative views here
admin.add_view(ModelView(Category, db_session))
admin.add_view(ModelView(Customers, db_session))

if __name__ == "__main__":
    app.run()
