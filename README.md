# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-06 13:53:05 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `39.66 ms` | `109.5 ms` | `185.58 ms` | `96.15%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `44.7 ms` | `47.73 ms` | `70.24 ms` | `96.15%` |
| **HuggingFace API** | `200 OK` | `164.16 ms` | `104.08 ms` | `143.64 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `264.53 ms` | `273.34 ms` | `384.23 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1793973186)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
