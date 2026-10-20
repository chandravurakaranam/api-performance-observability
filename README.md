# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-20 11:04:08 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `179.19 ms` | `118.56 ms` | `178.81 ms` | `88.89%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `60.35 ms` | `44.72 ms` | `59.79 ms` | `88.89%` |
| **HuggingFace API** | `200 OK` | `142.02 ms` | `108.14 ms` | `138.13 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `240.86 ms` | `412.94 ms` | `1598.88 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1792494249)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
