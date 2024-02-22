from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(f"{os.getenv("ENGINE")}://{os.getenv("DATABASE_USER")}:@{os.getenv("DATABASE_HOST")}:{os.getenv("DATABASE_PORT")}/{os.getenv("DATABASE_NAME")}", echo=False)

try:
    connection = engine.connect()
    print("Database connected!")
except Exception as e:
    print(str(e))

Session = sessionmaker(bind=engine)
session = Session()