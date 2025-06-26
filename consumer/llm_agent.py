# import os
# # from dotenv import load_dotenv
# # import openai
# # from openai import OpenAI
# import time
# from test import summarize_with_ollama

# # load_dotenv(dotenv_path=".env")


# # openai.api_key = os.getenv("OPENAI_API_KEY")

# # client = OpenAI()

# def summarize_market(data: dict) -> str:
#     prompt = "Recent market activity:\n"
#     for symbol, stat in data.items():
#         prompt += f"{symbol}: from {stat['start']} to {stat['end']}, Δ {stat['change']} ({stat['percent_change']}%)\n"

#     # Retry logic for rate limits
#     for i in range(5):
#             response=summarize_with_ollama(prompt)
#             return response
