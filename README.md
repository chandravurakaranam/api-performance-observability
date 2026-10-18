# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-18 16:38:14 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `415 FAIL` | `165.98 ms` | `172.11 ms` | `177.63 ms` | `50.0%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `37.54 ms` | `48.24 ms` | `57.88 ms` | `50.0%` |
| **HuggingFace API** | `200 OK` | `115.68 ms` | `112.05 ms` | `115.32 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `184.03 ms` | `209.56 ms` | `232.54 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
