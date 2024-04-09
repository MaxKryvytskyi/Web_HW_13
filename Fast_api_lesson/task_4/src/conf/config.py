from pydantic import BaseSettings
from decouple import config

class Settings(BaseSettings):
    sqlalchemy_database_url: str = config("SQLALCHEMY_DATABASE_URL")
    secret_key: str = config("SECRET_KEY")
    algorithm: str = config("ALGORITHM")
    mail_username: str = config("MAIL_USERNAME")
    mail_password: str = config("MAIL_PASSWORD")
    mail_from: str = config("MAIL_FROM")
    mail_port: int = config("MAIL_PORT")
    mail_server: str = config("MAIL_SERVER")
    redis_host: str = config("REDIS_HOST")
    redis_port: int = config("REDIS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
