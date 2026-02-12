from fastapi import FastAPI
from .database import engine, Base
from .models import Task

app = FastAPI()

# cria as tabelas
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "API funcionando"}
