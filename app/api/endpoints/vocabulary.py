from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database
import uuid

router = APIRouter()

@router.post("/", response_model=schemas.WordResponse)
def create_word(word: schemas.WordCreate, db: Session = Depends(database.get_db)):
    return crud.create_vocabulary(db=db, word=word)



@router.get("/{word_id}", response_model=schemas.WordResponse)
def read_word(word_id: str, db: Session = Depends(database.get_db)):
    db_word = crud.get_word(db, word_id=word_id)
    if db_word is None:
        raise HTTPException(status_code=404, detail="Word not found")
    return db_word

@router.patch("/{word_id}", response_model=schemas.WordResponse)
def update_word(word_id: str, word: schemas.WordUpdate, db: Session = Depends(database.get_db)):
    return crud.update_vocabulary(db, word_id, word)



@router.patch("/{word_id}/assets", response_model=schemas.WordResponse)
def update_asset(word_id: str, asset: schemas.AssetUpdate, db: Session = Depends(database.get_db)):
    return crud.update_asset_cache(db, word_id, asset)



@router.delete("/{word_id}")
def delete_word(word_id: str, db: Session = Depends(database.get_db)):
    crud.soft_delete(db, word_id)
    return {"message": "Soft deleted successfully"}