from pydantic import BaseModel
from typing import List


class Word(BaseModel):
    word:str
    meaning:str
    synonyms:List[str]

    