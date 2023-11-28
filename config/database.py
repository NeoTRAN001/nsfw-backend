
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import decl_base
from sqlalchemy.ext.declarative import declarative_base

load_dotenv(".env")

database_url = 'postgresql+psycopg2://{}:{}@{}:{}/{}?ssl=true'.format(
    os.getenv('DB_USERNAME'),
    os.getenv('DB_PASSWORD'),
    os.getenv('HOST'),
    os.getenv('DB_PORT'),
    os.getenv('DATABASE')
)
engine: Engine = create_engine(database_url)
Session: sessionmaker = sessionmaker(bind=engine)
Base: decl_base = declarative_base()


def db_config():
    Base.metadata.create_all(bind=engine)
