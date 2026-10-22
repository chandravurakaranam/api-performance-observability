# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-22 11:20:19 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `36.55 ms` | `111.46 ms` | `178.72 ms` | `90.91%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `34.4 ms` | `44.37 ms` | `59.65 ms` | `90.91%` |
| **HuggingFace API** | `200 OK` | `65.22 ms` | `107.51 ms` | `143.1 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `227.27 ms` | `378.9 ms` | `1372.54 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1792668020)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
