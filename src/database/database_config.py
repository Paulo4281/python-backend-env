from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:@localhost:3306/python_back_env", echo=False)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()