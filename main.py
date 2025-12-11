# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from databasecloud import SessionLocal, engine, Base
from crud import create_survey_response, get_all_responses
from schemas import SurveyResponseCreate, SurveyResponseRead
from typing import List

# Create FastAPI instance
app = FastAPI(title="Survey API")  # <-- this must be before any @app.get/@app.post

# Root endpoint for health check
@app.get("/")
def root():
    return {"status": "ok"}


# Create tables if they don’t exist
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST endpoint to submit a survey response
@app.post("/survey", response_model=SurveyResponseRead)
def submit_survey(survey: SurveyResponseCreate, db: Session = Depends(get_db)):
    return create_survey_response(db, survey)

# GET endpoint to list all survey responses
@app.get("/survey", response_model=List[SurveyResponseRead])
def list_surveys(db: Session = Depends(get_db)):
    return get_all_responses(db)
