# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-14 13:07:41 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `82.02 ms` | `99.8 ms` | `184.34 ms` | `97.06%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `34.36 ms` | `45.45 ms` | `68.11 ms` | `97.06%` |
| **HuggingFace API** | `200 OK` | `131.69 ms` | `100.56 ms` | `149.39 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `101.36 ms` | `232.12 ms` | `320.39 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1794661662)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
