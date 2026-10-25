# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-25 10:55:27 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `110.66 ms` | `110.64 ms` | `178.57 ms` | `92.86%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `55.29 ms` | `46.62 ms` | `65.22 ms` | `92.86%` |
| **HuggingFace API** | `200 OK` | `106.88 ms` | `104.2 ms` | `142.78 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `164.71 ms` | `357.22 ms` | `1152.16 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1792925728)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
