from sqlalchemy.orm import Session
from app import models, schemas  # To'liq import

def get_word(db: Session, word_id: str):
    return db.query(models.Vocabulary).filter(models.Vocabulary.word_id == word_id).first()

def create_vocabulary(db: Session, word: schemas.WordCreate):
    # Pydantic modelni dict ga o'tkazish (v2 da model_dump)
    db_word = models.Vocabulary(**word.model_dump())
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word

def update_vocabulary(db: Session, word_id: str, word_data: schemas.WordUpdate):
    db_query = db.query(models.Vocabulary).filter(models.Vocabulary.word_id == word_id)
    if db_query.first():
        db_query.update(word_data.model_dump(exclude_unset=True), synchronize_session=False)
        db.commit()
    return db_query.first()

def update_asset_cache(db: Session, word_id: str, asset: schemas.AssetUpdate):
    db_word = get_word(db, word_id)
    if db_word:
        db_word.telegram_file_id = asset.telegram_file_id
        db.commit()
        db.refresh(db_word)
    return db_word

def soft_delete(db: Session, word_id: str):
    db_word = get_word(db, word_id)
    if db_word:
        db_word.is_active = False
        db.commit()
    return db_word