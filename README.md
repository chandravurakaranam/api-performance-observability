# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-10 14:29:29 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `36.12 ms` | `105.28 ms` | `184.96 ms` | `96.67%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `31.36 ms` | `47.31 ms` | `69.18 ms` | `96.67%` |
| **HuggingFace API** | `200 OK` | `49.04 ms` | `101.8 ms` | `147.31 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `57.32 ms` | `251.58 ms` | `352.31 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1794320970)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
