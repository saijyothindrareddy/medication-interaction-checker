from fastapi import FastAPI, Body
from app.interaction_engine import check_interactions  # Make sure this import path is correct

app = FastAPI()

@app.post("/check")
def check(medications: dict = Body(...)):
    return check_interactions(medications)
