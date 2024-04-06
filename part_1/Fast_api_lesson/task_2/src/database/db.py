from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.my_config import MyConfig
import configparser

config = configparser.ConfigParser()
config.read('src/config/config.ini')

# SQLALCHEMY_DATABASE_URL = config.get('Security', 'SQLALCHEMY_DATABASE_URL')
SQLALCHEMY_DATABASE_URL = MyConfig.SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()