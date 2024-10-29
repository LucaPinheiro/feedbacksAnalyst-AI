from app.config import get_text_analytics_client
from app.schemas.feedback_schema import FeedbackResponse

def analyze_feedback(feedback_text: str) -> FeedbackResponse:
    client = get_text_analytics_client()
    response = client.analyze_sentiment([feedback_text])[0]
    
    sentiment = response.sentiment
    confidence_scores = {
        "positivo": response.confidence_scores.positive,
        "neutro": response.confidence_scores.neutral,
        "negativo": response.confidence_scores.negative
    }
    main_confidence = max(confidence_scores.values())
    
    return FeedbackResponse(
        sentimento=sentiment,
        pontuacao_confiança=confidence_scores,
        principal_confiança=main_confidence
    )
