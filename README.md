# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-19 15:24:09 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `125.64 ms` | `95.8 ms` | `183.57 ms` | `97.44%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `36.34 ms` | `43.93 ms` | `68.56 ms` | `97.44%` |
| **HuggingFace API** | `200 OK` | `109.39 ms` | `97.64 ms` | `149.2 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `132.02 ms` | `214.85 ms` | `280.49 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1795101850)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
