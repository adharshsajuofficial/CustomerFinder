from pydantic import BaseModel, Field
from typing import List

class EventInput(BaseModel):
    title: str = Field(min_length=2, max_length=160)
    description: str = ""
    city: str = ""
    interests: List[str] = []
    skills: List[str] = []
    event_type: str = "other"
    max_results: int = Field(default=10, ge=1, le=100)

class MatchRequest(BaseModel):
    event: EventInput
