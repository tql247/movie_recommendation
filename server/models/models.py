from pydantic import BaseModel
from typing import List
from datetime import date


class Location(BaseModel):
    locations: List
    date: date
