from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.getenv("AZURE_TEXT_ANALYTICS_ENDPOINT")
api_key = os.getenv("AZURE_TEXT_ANALYTICS_KEY")

def get_text_analytics_client():
    credential = AzureKeyCredential(api_key)
    client = TextAnalyticsClient(endpoint=endpoint, credential=credential)
    return client
