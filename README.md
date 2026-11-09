# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-09 15:29:03 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `102.48 ms` | `107.66 ms` | `185.12 ms` | `96.55%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `46.04 ms` | `47.86 ms` | `69.44 ms` | `96.55%` |
| **HuggingFace API** | `200 OK` | `101.3 ms` | `103.62 ms` | `147.59 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `162.63 ms` | `258.28 ms` | `360.29 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1794238144)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
