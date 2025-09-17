from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Workout Planner API")

# Workouts
@app.get("/workouts", response_model=list[schemas.Workout])
def read_workouts(db: Session = Depends(get_db)):
    return crud.get_workouts(db)

@app.get("/workouts/{workout_id}", response_model=schemas.Workout)
def read_workout(workout_id: int, db: Session = Depends(get_db)):
    db_workout = crud.get_workout(db, workout_id)
    if not db_workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    return db_workout

@app.post("/workouts", response_model=schemas.Workout)
def create_workout(workout: schemas.WorkoutCreate, db: Session = Depends(get_db)):
    return crud.create_workout(db, workout)

# Plans
@app.get("/plans/{user_id}", response_model=list[schemas.Plan])
def read_plans(user_id: int, db: Session = Depends(get_db)):
    return crud.get_plans(db, user_id)

@app.post("/plans", response_model=schemas.Plan)
def create_plan(plan: schemas.PlanCreate, db: Session = Depends(get_db)):
    return crud.create_plan(db, plan)
