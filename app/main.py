from fastapi import FastAPI
from app.api.endpoints import vocabulary
from app.database import engine
from app import models

# MB jadvallarini yaratish
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vocabulary Content Microservice", version="0.1.0")

# Routerni ulash
app.include_router(vocabulary.router, prefix="/v1/vocabulary", tags=["vocabulary"])

@app.get("/")
def root():
    return {"message": "Microservice is running"}