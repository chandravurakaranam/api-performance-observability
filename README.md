# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-27 16:18:56 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `102.99 ms` | `92.1 ms` | `182.04 ms` | `97.87%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `41.07 ms` | `41.15 ms` | `67.64 ms` | `97.87%` |
| **HuggingFace API** | `200 OK` | `135.82 ms` | `96.8 ms` | `147.64 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `109.37 ms` | `207.92 ms` | `344.91 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1795796337)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
