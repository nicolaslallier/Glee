from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello() -> dict[str, str]:
    return {"message": "hello world"}


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


def run():
    import uvicorn
    uvicorn.run("glee.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    run()
