# # Using Configuration Objects

from flask import Flask
# from config import DevelopmentConfig, TestingConfig, ProductionConfig

app = Flask(__name__)
# app.config.from_object(DevelopmentConfig)

# # Loading Configuration using environment variable

# import os
# from flask import Flask

# app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','default_secret')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///default.db')

# Using Flask.config.from_object() and Flask.config.from_envvar(): 

# from_object()
app.config.from_object('config.ProductionConfig')

# from_envvar()
import os

app.config.from_envvar('FLASK_CONFIG_FILE')
