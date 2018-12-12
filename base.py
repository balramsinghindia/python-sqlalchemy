# coding=utf-8

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mssql+pyodbc://{}:{}@{}:{}/{}?driver=ODBC+Driver+17+for+SQL+Server".format(
                "sa",
                "<YourStrong!Passw0rd>",
                "127.0.0.1",
                "1433",
                'master'))

Session = sessionmaker(bind=engine)

Base = declarative_base()
