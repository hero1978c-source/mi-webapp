from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/")
def root():
    return {"status": "ok", "mensaje": "Mi WebApp funcionando"}