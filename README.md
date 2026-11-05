# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-05 14:11:56 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `47.97 ms` | `112.29 ms` | `185.74 ms` | `96.0%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `44.62 ms` | `47.85 ms` | `70.51 ms` | `96.0%` |
| **HuggingFace API** | `200 OK` | `84.56 ms` | `101.68 ms` | `140.07 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `108.96 ms` | `273.69 ms` | `391.21 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1793887916)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
