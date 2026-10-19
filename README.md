# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-19 12:26:58 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `33.99 ms` | `121.94 ms` | `176.87 ms` | `85.71%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `43.59 ms` | `43.26 ms` | `55.44 ms` | `85.71%` |
| **HuggingFace API** | `200 OK` | `47.62 ms` | `102.51 ms` | `129.48 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `35.09 ms` | `488.02 ms` | `1823.49 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1792412818)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
