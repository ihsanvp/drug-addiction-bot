from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models import AddictionDetector, RecommendationSystem

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GetStageNameData(BaseModel):
    stage: str

@app.post("/stage")
def get_stage(data: GetStageNameData):
    detector = AddictionDetector()
    stage_name = detector.stages.get(data.stage, None)
    if stage_name is None:
        raise HTTPException(400, detail="Invalid stage")
    return {
        "stage": data.stage,
        "name": stage_name,
    }

class DetectStageData(BaseModel):
    answers: list[str]

@app.post("/detect-stage")
def detect_stage(data: DetectStageData):
    detector = AddictionDetector()
    stage = detector.detect_addiction_stage(data.answers)

    return {
        "stage": stage,
    }

class RecommendSolutionsData(BaseModel):
    stage: str

@app.post("/recommend-solutions")
def recommend_solutions(data: RecommendSolutionsData):
    recommendation_system = RecommendationSystem()
    solutions = recommendation_system.recommend_solution(data.stage)

    return {
        "solutions": solutions
    }
