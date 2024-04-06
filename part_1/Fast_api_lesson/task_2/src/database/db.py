from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from part_1.Fast_api_lesson.task_2.src.config.my_config import MyConfig


SQLALCHEMY_DATABASE_URL = MyConfig.SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()