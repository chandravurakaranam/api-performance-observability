# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-18 16:55:02 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `173.68 ms` | `172.63 ms` | `177.78 ms` | `66.67%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `47.25 ms` | `47.91 ms` | `57.78 ms` | `66.67%` |
| **HuggingFace API** | `200 OK` | `122.71 ms` | `115.6 ms` | `122.01 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `2504.23 ms` | `974.45 ms` | `2277.32 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
