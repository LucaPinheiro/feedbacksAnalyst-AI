from app.core.helpers.errors.controller_errors import MissingParameters
from app.core.helpers.external_interfaces import BadRequest, InternalServerError
from app.services.sentiment_service import analyze_feedback
from app.schemas.feedback_schema import FeedbackResponse

def get_feedback_analysis(feedback_text: str) -> FeedbackResponse:
    try:
        if not feedback_text:
            raise MissingParameters("feeedback")
        return analyze_feedback(feedback_text)
    
    except MissingParameters as e:
      return BadRequest(body=e.message)
    except Exception as e:
        return InternalServerError(body=str(e)) 