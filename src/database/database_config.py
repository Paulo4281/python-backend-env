from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(f"{os.getenv("ENGINE")}://{os.getenv("USER")}:@{os.getenv("DATABASE_HOST")}:{os.getenv("DATABASE_PORT")}/{os.getenv("DATABASE")}", echo=False)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()