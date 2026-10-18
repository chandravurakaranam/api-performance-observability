# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-18 17:12:16 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `111.01 ms` | `140.99 ms` | `177.33 ms` | `80.0%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `39.88 ms` | `44.04 ms` | `56.61 ms` | `80.0%` |
| **HuggingFace API** | `200 OK` | `132.29 ms` | `109.41 ms` | `130.37 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `149.4 ms` | `638.69 ms` | `2050.4 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1792343536)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
