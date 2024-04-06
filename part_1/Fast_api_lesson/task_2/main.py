
# from pathlib import Path

# import uvicorn
# from fastapi import FastAPI, BackgroundTasks
# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
# from pydantic import EmailStr, BaseModel
# from my_config import MyConfig


# class EmailSchema(BaseModel):
#     email: EmailStr


# conf = ConnectionConfig(
#     MAIL_USERNAME=str(MyConfig.MAIL_USERNAME[0]),
#     MAIL_PASSWORD=str(MyConfig.MAIL_PASSWORD[0]),
#     MAIL_FROM=str(MyConfig.MAIL_FROM[0]),
#     MAIL_PORT=int(MyConfig.MAIL_PORT[0]),
#     MAIL_SERVER=str(MyConfig.MAIL_SERVER[0]),
#     MAIL_FROM_NAME=str(MyConfig.MAIL_FROM_NAME[0]),
#     MAIL_STARTTLS=False,
#     MAIL_SSL_TLS=True,
#     USE_CREDENTIALS=True,
#     VALIDATE_CERTS=True,
#     TEMPLATE_FOLDER=Path(__file__).parent / 'templates',
# )

# app = FastAPI()


# @app.post("/send-email")
# async def send_in_background(background_tasks: BackgroundTasks, body: EmailSchema):
#     message = MessageSchema(
#         subject="Fastapi mail module",
#         recipients=[body.email],
#         template_body={"fullname": "Max Kryvytskyi"},
#         subtype=MessageType.html
#     )

#     fm = FastMail(conf)

#     background_tasks.add_task(fm.send_message, message, template_name="example_email.html")

#     return {"message": "email has been sent"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)



import uvicorn
from fastapi import FastAPI

from src.routes import notes, tags, auth

app = FastAPI()

app.include_router(auth.router, prefix='/api')
app.include_router(tags.router, prefix='/api')
app.include_router(notes.router, prefix='/api')


@app.get("/")
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)