# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-16 15:06:27 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `42.11 ms` | `96.07 ms` | `184.04 ms` | `97.22%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `17.58 ms` | `44.13 ms` | `67.58 ms` | `97.22%` |
| **HuggingFace API** | `200 OK` | `58.62 ms` | `98.18 ms` | `149.32 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `93.01 ms` | `223.01 ms` | `304.43 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1794841587)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
