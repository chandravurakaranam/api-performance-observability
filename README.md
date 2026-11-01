# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-01 12:50:11 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `33.96 ms` | `115.85 ms` | `186.36 ms` | `95.24%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `29.83 ms` | `48.2 ms` | `71.57 ms` | `95.24%` |
| **HuggingFace API** | `200 OK` | `48.28 ms` | `102.7 ms` | `142.02 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `131.56 ms` | `305.87 ms` | `424.13 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1793537412)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
