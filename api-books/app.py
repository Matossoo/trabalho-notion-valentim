import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from db import db
from models.book import Book

# Carrega as variáveis declaradas no arquivo .env
load_dotenv()

app = Flask(__name__)

# Pega a URL do banco do arquivo .env
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate(app, db)