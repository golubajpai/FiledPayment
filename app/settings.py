from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.views import *
from src.models import Card_details
from flask_marshmallow import Marshmallow
from src.config import DevConfig

app=Flask(__name__)
app.config.from_object(DevConfig)

app.add_url_rule('/payment/',view_func=ProcessPayment.as_view('payment'))
db = SQLAlchemy(app)
ma=Marshmallow(app)


migrate = Migrate(app, db)

