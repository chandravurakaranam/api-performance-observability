# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-30 12:19:32 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `98.18 ms` | `115.99 ms` | `183.57 ms` | `94.74%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `44.2 ms` | `48.86 ms` | `71.84 ms` | `94.74%` |
| **HuggingFace API** | `200 OK` | `111.8 ms` | `105.06 ms` | `142.24 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `148.08 ms` | `319.6 ms` | `632.14 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1793362773)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
