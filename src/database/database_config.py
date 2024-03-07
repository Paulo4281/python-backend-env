from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os import getenv

load_dotenv()

engine = create_engine(f"{getenv("ENGINE")}://{getenv("DATABASE_USER")}:@{getenv("DATABASE_HOST")}:{getenv("DATABASE_PORT")}/{getenv("DATABASE_NAME")}", echo=False)

print("Trying to connect to the database...")
try:
    connection = engine.connect()
    print("Database connected!")
except Exception as e:
    print("Not able to connect to the database.")
    print(str(e))

Session = sessionmaker(bind=engine)
session = Session()