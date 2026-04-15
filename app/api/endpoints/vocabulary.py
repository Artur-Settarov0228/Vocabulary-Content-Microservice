from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app import crud, schemas, database

router = APIRouter()  # ❗ BU YERDA PREFIX YO‘Q


@router.post("/", response_model=schemas.WordResponse, status_code=status.HTTP_201_CREATED)
def create_word(
    word: schemas.WordCreate,
    db: Session = Depends(database.get_db)
):
    return crud.create_vocabulary(db=db, word=word)


@router.patch("/{word_id}/assets", response_model=schemas.WordResponse)
def update_asset(
    word_id: int,
    asset: schemas.AssetUpdate,
    db: Session = Depends(database.get_db)
):
    db_word = crud.update_asset_cache(db, word_id, asset)

    if not db_word:
        raise HTTPException(status_code=404, detail="Word not found")

    return db_word


@router.get("/{word_id}", response_model=schemas.WordResponse)
def read_word(word_id: int, db: Session = Depends(database.get_db)):
    db_word = crud.get_word(db, word_id=word_id)
    if not db_word:
        raise HTTPException(status_code=404, detail="Word not found")
    return db_word

@router.patch("/{word_id}", response_model=schemas.WordResponse)
def update_word(
    word_id: int,
    word: schemas.WordUpdate,
    db: Session = Depends(database.get_db)
):
    db_word = crud.update_vocabulary(db, word_id, word)

    if not db_word:
        raise HTTPException(status_code=404, detail="Word not found")

    return db_word


@router.delete("/{word_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_word(
    word_id: int,
    db: Session = Depends(database.get_db)
):
    deleted = crud.soft_delete(db, word_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Word not found")

    return None