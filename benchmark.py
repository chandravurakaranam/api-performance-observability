import os
import time
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timezone

# Target endpoints and their specific header requirements
ENDPOINTS = {
    "GitHub API": {
        "url": "https://api.github.com",
        "headers": {"User-Agent": "Mozilla/5.0 (Automated Benchmarking Bot)"}
    },
    "Cloudflare DNS (1.1.1.1)": {
        "url": "https://1.1.1.1/dns-query?name=github.com",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Automated Benchmarking Bot)",
            "Accept": "application/dns-json"
        }
    },
    "HuggingFace API": {
        "url": "https://huggingface.co/api/models?limit=1",
        "headers": {"User-Agent": "Mozilla/5.0 (Automated Benchmarking Bot)"}
    },
    "HTTPBin Echo": {
        "url": "https://httpbin.org/get",
        "headers": {"User-Agent": "Mozilla/5.0 (Automated Benchmarking Bot)"}
    }
}

CSV_FILE = "history.csv"

# ==========================================
# 1. RUN BENCHMARKS
# ==========================================
current_timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
date_key = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")

results = []

for name, config in ENDPOINTS.items():
    url = config["url"]
    headers = config["headers"]
    try:
        start_time = time.time()
        response = requests.get(url, headers=headers, timeout=10)
        latency_ms = round((time.time() - start_time) * 1000, 2)
        status_code = response.status_code
        payload_size = len(response.content)
        success = 1 if status_code == 200 else 0
    except Exception:
        latency_ms = np.nan
        status_code = 0
        payload_size = 0
        success = 0

    results.append({
        "timestamp": date_key,
        "service": name,
        "latency_ms": latency_ms,
        "status_code
