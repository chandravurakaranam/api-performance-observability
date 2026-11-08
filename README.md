# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-08 12:55:12 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `136.93 ms` | `107.85 ms` | `185.28 ms` | `96.43%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `60.53 ms` | `47.92 ms` | `69.71 ms` | `96.43%` |
| **HuggingFace API** | `200 OK` | `149.87 ms` | `103.7 ms` | `147.88 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `162.42 ms` | `261.7 ms` | `368.27 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1794142513)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
