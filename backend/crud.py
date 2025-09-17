from sqlalchemy.orm import Session
import models, schemas

# Workout CRUD
def get_workouts(db: Session):
    return db.query(models.Workout).all()

def get_workout(db: Session, workout_id: int):
    return db.query(models.Workout).filter(models.Workout.id == workout_id).first()

def create_workout(db: Session, workout: schemas.WorkoutCreate):
    db_workout = models.Workout(**workout.dict())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

# Plan CRUD
def get_plans(db: Session, user_id: int):
    return db.query(models.Plan).filter(models.Plan.user_id == user_id).all()

def create_plan(db: Session, plan: schemas.PlanCreate):
    db_plan = models.Plan(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan
