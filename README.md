# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-27 11:45:21 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `183.26 ms` | `115.01 ms` | `180.21 ms` | `93.75%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `54.13 ms` | `48.65 ms` | `72.24 ms` | `93.75%` |
| **HuggingFace API** | `200 OK` | `98.93 ms` | `104.56 ms` | `142.56 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `259.52 ms` | `341.51 ms` | `944.16 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1793101522)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
