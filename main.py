from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/institute/", response_model=schemas.InstituteCreate)
def create_institute(institute: schemas.InstituteCreate, db: Session = Depends(get_db)):
    return crud.create_institute(db=db, institute=institute)

@app.get("/search/")
def search(query: str, db: Session = Depends(get_db)):
    result = []
    institutes = crud.get_institute_by_name(db, query)
    # similar queries for courses and students
    return result
