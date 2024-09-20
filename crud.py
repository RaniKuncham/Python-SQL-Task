from sqlalchemy.orm import Session
from . import models, schemas

def create_institute(db: Session, institute: schemas.InstituteCreate):
    db_institute = models.Institute(institute_name=institute.institute_name)
    db.add(db_institute)
    db.commit()
    db.refresh(db_institute)
    return db_institute

def get_institute_by_name(db: Session, name: str):
    return db.query(models.Institute).filter(models.Institute.institute_name.ilike(f"%{name}%")).all()

# Similarly, add CRUD functions for Course and Student.
