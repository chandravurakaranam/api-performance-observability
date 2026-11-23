# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-23 17:36:15 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `92.02 ms` | `92.54 ms` | `182.85 ms` | `97.67%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `40.13 ms` | `42.31 ms` | `68.03 ms` | `97.67%` |
| **HuggingFace API** | `200 OK` | `110.75 ms` | `96.49 ms` | `148.64 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `158.82 ms` | `214.34 ms` | `367.88 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1795455376)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
