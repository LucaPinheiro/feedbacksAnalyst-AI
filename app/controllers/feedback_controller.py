from app.services.sentiment_service import analyze_feedback
from app.schemas.feedback_schema import FeedbackResponse

def get_feedback_analysis(feedback_text: str) -> FeedbackResponse:
    return analyze_feedback(feedback_text)
