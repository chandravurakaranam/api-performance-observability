# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-17 15:38:46 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `129.26 ms` | `96.97 ms` | `183.88 ms` | `97.3%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `68.23 ms` | `44.78 ms` | `68.9 ms` | `97.3%` |
| **HuggingFace API** | `200 OK` | `128.98 ms` | `99.02 ms` | `149.28 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `172.29 ms` | `221.64 ms` | `296.45 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1794929927)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
