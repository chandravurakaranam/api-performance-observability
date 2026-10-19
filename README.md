# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-19 16:54:10 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `34.32 ms` | `110.99 ms` | `176.64 ms` | `87.5%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `39.31 ms` | `42.77 ms` | `54.86 ms` | `87.5%` |
| **HuggingFace API** | `200 OK` | `113.61 ms` | `103.9 ms` | `129.01 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `59.44 ms` | `434.45 ms` | `1710.03 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1792428851)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
