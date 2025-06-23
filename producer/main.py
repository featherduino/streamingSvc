import json, random, time, os
from datetime import datetime
from kafka import KafkaProducer
from dotenv import load_dotenv

load_dotenv()

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

SYMBOLS = ["RELIANCE", "TCS", "INFY", "SBIN", "HDFCBANK"]

def generate_tick():
    sym = random.choice(SYMBOLS)
    ltp = round(random.uniform(2500, 3000), 2)
    return {
        "symbol": sym,
        "ltp": ltp,
        "timestamp": datetime.utcnow().isoformat(),
        "source": "mock"
    }

while True:
    tick = generate_tick()
    producer.send("market_ticks", tick)
    print("[Produced]", tick)
    time.sleep(1)
