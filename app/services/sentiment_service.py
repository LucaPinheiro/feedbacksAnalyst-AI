from app.config import get_text_analytics_client
from app.schemas.feedback_schema import FeedbackResponse

def preprocess_text(feedback_text: str) -> str:
    list_not = ['nao', 'não', 'n']
    negative_phrases = [f"{word} gostei" for word in list_not] + [f"{word} recomendo" for word in list_not] + [ "péssimo", "horrível", "detestei"]
    for phrase in negative_phrases:
        if phrase in feedback_text.lower():
            return "negative"
    return feedback_text

def analyze_feedback(feedback_text: str) -> FeedbackResponse:
    feedback_text = preprocess_text(feedback_text)

    client = get_text_analytics_client()
    sentiment_response = client.analyze_sentiment([feedback_text])[0]

    sentiment = "negative" if feedback_text == "negative" else sentiment_response.sentiment
    
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
