import uvicorn
from src.routes import notes, tags, auth
from src.services.limiter import app, limiter
from fastapi import Request


app.include_router(auth.router, prefix='/api')
app.include_router(tags.router, prefix='/api')
app.include_router(notes.router, prefix='/api')


@app.get("/")
@limiter.limit("2/minute")
def read_root(request: Request):
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)



# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)