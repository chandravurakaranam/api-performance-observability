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
        "status_code": status_code,
        "payload_bytes": payload_size,
        "success": success
    })

df_new = pd.DataFrame(results)

# Append to cumulative dataset
if os.path.exists(CSV_FILE):
    df_history = pd.read_csv(CSV_FILE)
    df_combined = pd.concat([df_history, df_new], ignore_index=True)
else:
    df_combined = df_new

df_combined.to_csv(CSV_FILE, index=False)

# ==========================================
# 2. GENERATE LATENCY TIME-SERIES PLOT
# ==========================================
plt.figure(figsize=(10, 5))

for name in ENDPOINTS.keys():
    service_data = df_combined[df_combined["service"] == name].tail(30)
    plt.plot(service_data["timestamp"], service_data["latency_ms"], marker='o', label=name)

plt.title("API Latency Trends (Last 30 Runs)")
plt.xlabel("Execution Timestamp")
plt.ylabel("Latency (ms)")
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig("latency_trend.png", dpi=300)
plt.close()

# ==========================================
# 3. CALCULATE SLA METRICS & GENERATE README
# ==========================================
summary_rows = []
for name in ENDPOINTS.keys():
    service_df = df_combined[df_combined["service"] == name]
    avg_latency = round(service_df["latency_ms"].mean(), 2)
    p95_latency = round(np.nanpercentile(service_df["latency_ms"], 95), 2)
    uptime_pct = round((service_df["success"].sum() / len(service_df)) * 100, 2)
    latest_status = int(service_df.iloc[-1]["status_code"])
    latest_latency = service_df.iloc[-1]["latency_ms"]

    summary_rows.append({
        "Service": name,
        "Latest Status": f"`{latest_status} OK`" if latest_status == 200 else f"`{latest_status} FAIL`",
        "Current Latency": f"`{latest_latency} ms`",
        "Avg Latency": f"`{avg_latency} ms`",
        "P95 Latency": f"`{p95_latency} ms`",
        "SLA Uptime": f"`{uptime_pct}%`"
    })

summary_df = pd.DataFrame(summary_rows)

readme_markdown = f"""# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **{current_timestamp}**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
"""

for _, row in summary_df.iterrows():
    readme_markdown += f"| **{row['Service']}** | {row['Latest Status']} | {row['Current Latency']} | {row['Avg Latency']} | {row['P95 Latency']} | {row['SLA Uptime']} |\n"

readme_markdown += """
### Historical Latency Trend
![Latency Trends](latency_trend.png?v={int(time.time())})
"""


---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
"""

with open("README.md", "w") as f:
    f.write(readme_markdown)

print("Observability benchmark run complete.")
