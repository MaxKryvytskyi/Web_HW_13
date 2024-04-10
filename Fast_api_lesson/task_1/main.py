from pathlib import Path
import uvicorn
from fastapi import FastAPI, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from decouple import config
 
class EmailSchema(BaseModel):
    email: EmailStr


conf = ConnectionConfig(
    MAIL_USERNAME=config('MAIL_USERNAME'),
    MAIL_PASSWORD=config('MAIL_PASSWORD'),
    MAIL_FROM=config('MAIL_FROM'),
    MAIL_PORT=config('MAIL_PORT'),
    MAIL_SERVER=config('MAIL_SERVER'),
    MAIL_FROM_NAME=config('MAIL_FROM_NAME'),
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=Path(__file__).parent / 'templates',
)

app = FastAPI()


@app.post("/send-email")
async def send_in_background(background_tasks: BackgroundTasks, body: EmailSchema):
    print(body)
    message = MessageSchema(
        subject="Fastapi mail module",
        recipients=[body.email],
        template_body={"fullname": "Max Kryvytskyi"},
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    print(message)
    background_tasks.add_task(fm.send_message, message, template_name="example_email.html")

    return {"message": "email has been sent"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)