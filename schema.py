# schemas.py
from pydantic import BaseModel

# Schema for incoming survey submissions (POST requests)
class SurveyResponseCreate(BaseModel):
    name: str
    email: str
    feedback: str

# Schema for responses including the database ID (GET requests)
class SurveyResponse(SurveyResponseCreate):
    id: int

    class Config:
        orm_mode = True  # Allows Pydantic to read SQLAlchemy model objects
