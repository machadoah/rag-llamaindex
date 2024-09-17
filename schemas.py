from pydantic import BaseModel
from typing import Set


class Question(BaseModel):
    question: str


class Answer(BaseModel):
    answer: str


class Members(BaseModel):
    Members: Set[str]
