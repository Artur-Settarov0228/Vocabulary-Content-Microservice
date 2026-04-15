import uuid
from sqlalchemy import Column, String, Integer, Boolean, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class Vocabulary(Base):
    __tablename__ = "vocabulary"

    word_id = Column(Integer, primary_key=True, autoincrement=True) 
    english_word = Column(String, nullable=False)
    part_of_speech = Column(String, nullable=True)
    phonetic_transcription = Column(String, nullable=True)
    raw_storage_url = Column(String, nullable=False)
    telegram_file_id = Column(String, nullable=True) # Nullable bo'lishi shart
    level = Column(String(10), nullable=True)
    difficulty = Column(Integer, default=1)
    is_active = Column(Boolean, default=True) # Soft delete uchun
    created_at = Column(DateTime(timezone=True), server_default=func.now())