import os
from dotenv import load_dotenv
import openai
from openai import OpenAI
import time
load_dotenv(dotenv_path=".env")


openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

def summarize_market(data: dict) -> str:
    if not data:
        return "No movement detected."

    prompt = "Summarize today's tick data like a trading assistant:\n\n"
    for symbol, stat in data.items():
        prompt += f"{symbol}: from {stat['start']} to {stat['end']}, Δ {stat['change']} ({stat['percent_change']}%)\n"

    # Retry logic for rate limits
    for i in range(5):
        try:
            response = client.responses.create(
            model="gpt-4.1",
            input="You are a financial assistant and a geopolitics expert.")
            return response["choices"][0]["message"]["content"]

        except openai.RateLimitError:
            wait = 2 ** i
            print(f"Rate limit hit. Waiting {wait} seconds...")
            time.sleep(wait)

    return "Rate limit exceeded. Try again later."