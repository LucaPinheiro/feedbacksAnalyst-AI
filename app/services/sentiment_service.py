from app.config import get_text_analytics_client
from app.schemas.feedback_schema import FeedbackResponse

def analyze_feedback(feedback_text: str) -> FeedbackResponse:
    client = get_text_analytics_client()
    
    sentiment_response = client.analyze_sentiment([feedback_text])[0]
    sentiment = sentiment_response.sentiment
    confidence_scores = {
        "positivo": sentiment_response.confidence_scores.positive,
        "neutro": sentiment_response.confidence_scores.neutral,
        "negativo": sentiment_response.confidence_scores.negative
    }
    main_confidence = max(confidence_scores.values())
    
    key_phrases_response = client.extract_key_phrases([feedback_text])[0]
    key_phrases = key_phrases_response.key_phrases if not key_phrases_response.is_error else []

    analysis_summary = f"O principal motivo do feedback {'positivo' if sentiment == 'positive' else 'negativo'} parece ser: " + ", ".join(key_phrases)

    return FeedbackResponse(
        sentimento=sentiment,
        pontuacao_confiança=confidence_scores,
        principal_confiança=main_confidence,
        analise=analysis_summary
    )
