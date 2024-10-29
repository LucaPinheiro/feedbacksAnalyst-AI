from fastapi import APIRouter
from app.schemas.feedback_schema import FeedbackRequest, FeedbackResponse
from app.controllers.feedback_controller import get_feedback_analysis

router = APIRouter()

@router.post("/analyze-feedback/", response_model=FeedbackResponse)
async def analyze_feedback_endpoint(request: FeedbackRequest):
    return get_feedback_analysis(request.feedback)

@router.get("/health-check/")
async def health_check_endpoint():
    return {"status": "ok"}