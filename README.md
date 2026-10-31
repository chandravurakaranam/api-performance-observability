# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-31 11:50:18 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `194.91 ms` | `119.94 ms` | `186.79 ms` | `95.0%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `53.95 ms` | `49.12 ms` | `71.7 ms` | `95.0%` |
| **HuggingFace API** | `200 OK` | `112.26 ms` | `105.42 ms` | `142.13 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `219.32 ms` | `314.59 ms` | `528.14 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1793447420)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
