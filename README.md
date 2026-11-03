# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-03 13:47:16 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `92.98 ms` | `114.39 ms` | `186.05 ms` | `95.65%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `55.61 ms` | `48.09 ms` | `71.04 ms` | `95.65%` |
| **HuggingFace API** | `200 OK` | `119.19 ms` | `102.42 ms` | `141.05 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `128.17 ms` | `287.82 ms` | `407.67 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1793713637)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
