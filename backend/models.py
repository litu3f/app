from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = \"sqlite:///./jobs.db\"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

class Job(Base):
    __tablename__ = \"jobs\"
    id = Column(Integer, primary_key=True, index=True)
    original_file = Column(String)
    processed_file = Column(String)
    status = Column(String)
