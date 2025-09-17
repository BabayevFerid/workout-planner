from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Workout(Base):
    __tablename__ = "workouts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    type = Column(String, nullable=False)  # cardio/strength/flexibility
    duration = Column(Integer, nullable=False)  # minutes
    difficulty = Column(String, nullable=False)  # beginner/intermediate/advanced

class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    workout_id = Column(Integer, ForeignKey("workouts.id"))
    day = Column(String, nullable=False)
    workout = relationship("Workout")
