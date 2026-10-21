# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-21 11:20:37 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `122.47 ms` | `118.96 ms` | `178.76 ms` | `90.0%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `51.17 ms` | `45.36 ms` | `59.72 ms` | `90.0%` |
| **HuggingFace API** | `200 OK` | `144.18 ms` | `111.74 ms` | `143.21 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `224.21 ms` | `394.07 ms` | `1485.71 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1792581638)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
