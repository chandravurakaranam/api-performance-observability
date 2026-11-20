# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-20 15:00:39 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `58.99 ms` | `94.88 ms` | `183.42 ms` | `97.5%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `25.92 ms` | `43.48 ms` | `68.4 ms` | `97.5%` |
| **HuggingFace API** | `200 OK` | `93.57 ms` | `97.54 ms` | `149.17 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `82.63 ms` | `211.55 ms` | `272.51 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1795186840)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
