from fastapi import FastAPI
from src.routes import contact
from src.routes import auth 
from src.routes import users
import uvicorn

app = FastAPI()


app.include_router(auth.router, prefix='/api')
app.include_router(contact.router, prefix='/api')
app.include_router(users.router, prefix='/api')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)