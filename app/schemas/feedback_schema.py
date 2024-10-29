from pydantic import BaseModel
from typing import Dict, List

class FeedbackRequest(BaseModel):
    feedback: str

class FeedbackResponse(BaseModel):
    sentimento: str
    pontuacao_confiança: Dict[str, float]
    principal_confiança: float
    analise: str
