# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-18 17:15:07 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `114.65 ms` | `136.6 ms` | `177.1 ms` | `83.33%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `39.01 ms` | `43.21 ms` | `56.03 ms` | `83.33%` |
| **HuggingFace API** | `200 OK` | `122.91 ms` | `111.66 ms` | `129.94 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `187.6 ms` | `563.51 ms` | `1936.95 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1792343707)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
