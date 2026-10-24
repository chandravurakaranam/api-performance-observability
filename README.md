# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-24 10:29:02 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `124.3 ms` | `110.64 ms` | `178.62 ms` | `92.31%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `74.25 ms` | `45.95 ms` | `65.91 ms` | `92.31%` |
| **HuggingFace API** | `200 OK` | `97.47 ms` | `103.99 ms` | `142.88 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `424.13 ms` | `372.03 ms` | `1256.17 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1792837743)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
