# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-23 11:10:57 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `87.94 ms` | `109.5 ms` | `178.67 ms` | `91.67%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `35.11 ms` | `43.6 ms` | `59.58 ms` | `91.67%` |
| **HuggingFace API** | `200 OK` | `71.78 ms` | `104.53 ms` | `142.99 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `244.35 ms` | `367.69 ms` | `1261.3 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1792753858)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
