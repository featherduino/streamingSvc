from kafka import KafkaConsumer
import json
from analytics import update_symbol_data, analyze_ticks
from llm_agent import summarize_market
import time

consumer = KafkaConsumer(
    "market_ticks",
    bootstrap_servers="localhost:9092",
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    group_id="tick-consumer"
)

last_summary_ts = 0
SUMMARY_INTERVAL = 60

for msg in consumer:
    tick = msg.value
    update_symbol_data(tick)

    analysis = analyze_ticks()

    now = time.time()
    if analysis and now - last_summary_ts > SUMMARY_INTERVAL:
        summary = summarize_market(analysis)
        print("[🤖 SUMMARY]", summary)
        last_summary_ts = now
