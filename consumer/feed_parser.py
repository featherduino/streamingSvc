import feedparser
import datetime

FEED_URL = "https://www.espncricinfo.com/rss/content/story/feeds/1.xml"

feed = feedparser.parse(FEED_URL)

print(f"Feed title: {feed.feed.title}")
print("Latest entries:")
for entry in feed.entries[:20]:
    print(f"- {entry.title} ({entry.published})")
    print(f"  Link: {entry.link}")
    print()

rss_feeds = {
"https://www.espncricinfo.com/rss/content/story/feeds/1.xml",""
}

def summarize_with_ollama(text, model='mistral'):
    import requests
    prompt = f"Summarize the following news item in one sentence:\n\n{text}"
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )
    if response.status_code == 200:
        return response.json().get("message", {}).get("content", "⚠️ No content in response.")
    return f"⚠️ Failed to get summary. Status code: {response.status_code}"




def format_entry_for_ollama(entry):
    from datetime import datetime

    title = entry.get("title", "").strip()
    summary = entry.get("summary", "").strip()
    link = entry.get("link", "").strip()

    published = "Unknown date"
    if "published_parsed" in entry and entry["published_parsed"]:
        published = datetime(*entry.published_parsed[:6]).strftime('%Y-%m-%d %H:%M')

    # Optional: include media or images
    image = ""
    if "media_content" in entry and isinstance(entry["media_content"], list):
        image = entry["media_content"][0].get("url", "")

    return f"""Title: {title}
Published: {published}
Link: {link}

Summary:
{summary}

{f"Image: {image}" if image else ""}
"""


def fetch_news():
    print(f"\n🔄 Fetching news at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...\n")
    for  url in rss_feeds:
        feed = feedparser.parse("https://www.espncricinfo.com/rss/content/story/feeds/1.xml")
        # print(f"\n Source: {source} ({url})\n{'-'*60}")
        print(f"Feed title: {feed.feed.title}")
        print("Latest entries:")
        for entry in feed.entries[:20]:
            formatted_text = format_entry_for_ollama(entry)
            ollama_summary = summarize_with_ollama(formatted_text)
            # print(f"- {entry.title} ({entry.published})")
            print(f"  Link: {entry.link}")
            print()