# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-22 14:14:38 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `25.59 ms` | `92.56 ms` | `183.06 ms` | `97.62%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `17.79 ms` | `42.36 ms` | `68.13 ms` | `97.62%` |
| **HuggingFace API** | `200 OK` | `37.66 ms` | `96.15 ms` | `148.88 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `216.6 ms` | `215.66 ms` | `373.62 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1795356878)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
