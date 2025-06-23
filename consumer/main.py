from kafka import KafkaConsumer
import json
from analytics import update_symbol_data, analyze_ticks
from llm_agent import summarize_market



consumer = KafkaConsumer(
    "market_ticks",
    bootstrap_servers="localhost:9092",
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    group_id="tick-consumer"
)

for msg in consumer:
    tick = msg.value
    update_symbol_data(tick)

    analysis = analyze_ticks()
    # print("[📈 ANALYSIS]", analysis)

    # 🧠 Add condition so LLM doesn’t run on every tick
    if analysis:
        summary = summarize_market(analysis)
        print("[🤖 SUMMARY]", summary)

