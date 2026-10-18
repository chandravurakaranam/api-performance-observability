# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-18 17:06:28 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `76.02 ms` | `148.48 ms` | `177.56 ms` | `75.0%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `36.6 ms` | `45.08 ms` | `57.2 ms` | `75.0%` |
| **HuggingFace API** | `200 OK` | `67.97 ms` | `103.7 ms` | `121.66 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `120.71 ms` | `761.02 ms` | `2163.86 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1792343189)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
