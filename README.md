# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-29 12:28:15 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `79.14 ms` | `116.98 ms` | `183.72 ms` | `94.44%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `39.55 ms` | `49.12 ms` | `71.97 ms` | `94.44%` |
| **HuggingFace API** | `200 OK` | `98.26 ms` | `104.68 ms` | `142.34 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `256.44 ms` | `329.13 ms` | `736.14 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1793276896)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
