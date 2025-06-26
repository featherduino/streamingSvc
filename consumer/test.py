import feedparser
from datetime import datetime
import time
import requests

def summarize_with_ollama(stat, model='deepseek-r1:1.5b'):
    import requests
    import json

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": model,
            "messages": [
                {"role": "user", "content": stat}
            ]
        },
        stream=True
    )

    if response.status_code != 200:
        return f"⚠️ Failed to get summary. Status code: {response.status_code}"

    full_response = ""
    for line in response.iter_lines():
        if not line:
            continue
        try:
            chunk = json.loads(line.decode("utf-8"))
            full_response += chunk.get("message", {}).get("content", "")
            if chunk.get("done", False):
                break
        except json.JSONDecodeError:
            continue

    return full_response.strip() or "⚠️ No summary returned."





def summarize_market(data: dict) -> str:
    prompt = "Recent market activity:\n"
    for symbol, stat in data.items():
        prompt += f"{symbol}: from {stat['start']} to {stat['end']}, Δ {stat['change']} ({stat['percent_change']}%)\n"

    prompt += "\nSummarize this market activity in one sentence."

    for i in range(5):
        try:
            response = summarize_with_ollama(prompt)
            if response:
                return response
        except Exception as e:
            print(f"[⚠️ Retry {i+1}/5] Summarization failed: {e}")
            time.sleep(2 ** i)  # exponential backoff

    return "⚠️ Failed to summarize after multiple attempts."




# rss_feeds = {
# "https://www.espncricinfo.com/rss/content/story/feeds/1.xml",""
# }

# ecosystem_entities = {
#     "main": ["Servotech", "Servotech Power", "Servotech Renewable"],
#     "subsidiaries": ["SolarCity", "Maxwell Technologies", "Servotech Energy"],
#     "complementary": ["Panasonic", "ChargePoint", "Techbec Industries"],
#     "competitors": ["Tata Power", "Adani Energy", "BHEL", "Exide", "Amara Raja", "Okaya"]
# }

# all_keywords = {k: [x.lower() for x in v] for k, v in ecosystem_entities.items()}

# def categorize_article(title: str, summary: str):
#     title_lower = title.lower()
#     summary_lower = summary.lower()
    
#     for category, keywords in all_keywords.items():
#         for word in keywords:
#             if word in title_lower or word in summary_lower:
#                 return category
#     return "uncategorized"

# def format_entry_for_ollama(entry):
#     from datetime import datetime

#     title = entry.get("title", "").strip()
#     summary = entry.get("summary", "").strip()
#     link = entry.get("link", "").strip()

#     published = "Unknown date"
#     if "published_parsed" in entry and entry["published_parsed"]:
#         published = datetime(*entry.published_parsed[:6]).strftime('%Y-%m-%d %H:%M')

#     # Optional: include media or images
#     image = ""
#     if "media_content" in entry and isinstance(entry["media_content"], list):
#         image = entry["media_content"][0].get("url", "")

#     return f"""Title: {title}
# Published: {published}
# Link: {link}

# Summary:
# {summary}

# {f"Image: {image}" if image else ""}
# """




# def fetch_news():
#     print(f"\n🔄 Fetching news at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...\n")
#     for  url in rss_feeds:
#         feed = feedparser.parse("https://www.espncricinfo.com/rss/content/story/feeds/1.xml")
#         # print(f"\n Source: {source} ({url})\n{'-'*60}")
#         print(f"Feed title: {feed.feed.title}")
#         print("Latest entries:")
#         for entry in feed.entries[:20]:
#             formatted_text = format_entry_for_ollama(entry)
#             ollama_summary = summarize_with_ollama(formatted_text)
#             print(f"- {entry.title} ({entry.published})")
#             print(f"  Link: {entry.link}")
#             print(ollama_summary)
#             print()


# if __name__ == "__main__":
#     fetch_news()