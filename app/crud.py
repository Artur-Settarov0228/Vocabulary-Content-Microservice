from sqlalchemy.orm import Session
from uuid import UUID
from app import models, schemas


def create_vocabulary(db: Session, word: schemas.WordCreate):
    data = word.model_dump(mode="json")  # 🔥 BEST

    db_word = models.Vocabulary(**data)
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word


def get_word(db: Session, word_id: int):
    return db.query(models.Vocabulary).filter(models.Vocabulary.word_id == word_id).first()


def update_vocabulary(db: Session, word_id: UUID, word: schemas.WordUpdate):
    db_word = get_word(db, word_id)
    if not db_word:
        return None

    for key, value in word.model_dump(exclude_unset=True).items():
        setattr(db_word, key, value)

    db.commit()
    db.refresh(db_word)
    return db_word


def update_asset_cache(db: Session, word_id: int, asset: schemas.AssetUpdate):
    db_word = get_word(db, word_id)
    if db_word:
        db_word.telegram_file_id = asset.telegram_file_id
        db.commit()
        db.refresh(db_word)
    return db_word

def soft_delete(db: Session, word_id: int):
    db_word = get_word(db, word_id)
    if db_word:
        db_word.is_active = False
        db.commit()
    return db_word