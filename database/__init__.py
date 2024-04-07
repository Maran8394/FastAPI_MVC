
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "mysql+mysqldb://username:password@localhost/db_name"

engine = create_engine(DB_URL, echo=True, pool_pre_ping=True)  # echo=True for debugging, you can turn it off in production
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()