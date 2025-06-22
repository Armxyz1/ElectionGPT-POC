from sqlalchemy import create_engine
from langchain.utilities import SQLDatabase
from config import DATABASE_URL

def get_database():
    engine = create_engine(DATABASE_URL)
    return SQLDatabase(engine)
