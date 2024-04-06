from pathlib import Path
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from fastapi_mail.errors import ConnectionErrors
from pydantic import EmailStr

from src.services.auth import auth_service
from src.config.my_config import MyConfig


conf = ConnectionConfig(
    MAIL_USERNAME=str(MyConfig.MAIL_USERNAME[0]),
    MAIL_PASSWORD=str(MyConfig.MAIL_PASSWORD[0]),
    MAIL_FROM=str(MyConfig.MAIL_FROM[0]),
    MAIL_PORT=int(MyConfig.MAIL_PORT[0]),
    MAIL_SERVER=str(MyConfig.MAIL_SERVER[0]),
    MAIL_FROM_NAME=str(MyConfig.MAIL_FROM_NAME[0]),
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=Path(__file__).parent / 'templates',
)


async def send_email(email: EmailStr, username: str, host: str):
    try:
        token_verification = auth_service.create_email_token({"sub": email})
        message = MessageSchema(
            subject="Confirm your email ",
            recipients=[email],
            template_body={"host": host, "username": username, "token": token_verification},
            subtype=MessageType.html
        )

        fm = FastMail(conf)
        await fm.send_message(message, template_name="email_template.html")
    except ConnectionErrors as err:
        print(err)