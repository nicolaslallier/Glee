from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "hello world"}


@app.get("/health")
async def health():
    return {"status": "ok"}


def run():
    import uvicorn
    uvicorn.run("glee.main:app", host="0.0.0.0", port=8000, reload=True)
