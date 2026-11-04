# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-04 13:55:31 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `128.52 ms` | `114.97 ms` | `185.9 ms` | `95.83%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `45.77 ms` | `47.99 ms` | `70.77 ms` | `95.83%` |
| **HuggingFace API** | `200 OK` | `101.7 ms` | `102.39 ms` | `140.56 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `113.35 ms` | `280.55 ms` | `399.44 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1793800532)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
