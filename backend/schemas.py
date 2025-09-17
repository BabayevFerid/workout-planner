from pydantic import BaseModel

class WorkoutBase(BaseModel):
    name: str
    type: str
    duration: int
    difficulty: str

class WorkoutCreate(WorkoutBase):
    pass

class Workout(WorkoutBase):
    id: int
    class Config:
        orm_mode = True

class PlanBase(BaseModel):
    user_id: int
    workout_id: int
    day: str

class PlanCreate(PlanBase):
    pass

class Plan(PlanBase):
    id: int
    workout: Workout
    class Config:
        orm_mode = True
