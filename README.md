# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-25 16:54:54 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `65.08 ms` | `92.42 ms` | `182.45 ms` | `97.78%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `23.34 ms` | `41.64 ms` | `67.83 ms` | `97.78%` |
| **HuggingFace API** | `200 OK` | `74.01 ms` | `95.72 ms` | `148.14 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `103.85 ms` | `210.12 ms` | `356.39 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1795625695)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
