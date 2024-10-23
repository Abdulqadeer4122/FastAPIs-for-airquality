# app/main.py
from fastapi import FastAPI
from app.routes.route import router

app = FastAPI()

# Include the routes
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Air Quality API!"}
