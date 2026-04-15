from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from enum import Enum
from uuid import UUID


class PartOfSpeech(str, Enum):
    noun = "noun"
    verb = "verb"
    adjective = "adjective"


class Level(str, Enum):
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"


class WordBase(BaseModel):
    english_word: str = Field(..., min_length=1, max_length=100)
    part_of_speech: Optional[PartOfSpeech] = None
    phonetic_transcription: Optional[str] = Field(None, max_length=100)
    level: Level
    difficulty: int = Field(..., ge=1, le=10)


class WordCreate(WordBase):
    raw_storage_url: HttpUrl


class WordUpdate(BaseModel):
    english_word: Optional[str] = Field(None, min_length=1, max_length=100)
    part_of_speech: Optional[PartOfSpeech] = None
    level: Optional[Level] = None
    difficulty: Optional[int] = Field(None, ge=1, le=10)


class AssetUpdate(BaseModel):
    telegram_file_id: str = Field(..., min_length=5)


class WordResponse(WordBase):
    word_id: int
    raw_storage_url: HttpUrl
    telegram_file_id: Optional[str] = None
    is_active: bool

    class Config:
        from_attributes = True