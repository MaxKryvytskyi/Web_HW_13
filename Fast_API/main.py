from fastapi import FastAPI
from src.routes import contact
from src.routes import auth 
import uvicorn

app = FastAPI()


app.include_router(auth.router, prefix='/api')
app.include_router(contact.router, prefix='/api')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)