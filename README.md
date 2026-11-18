# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-18 15:16:19 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `22.68 ms` | `95.01 ms` | `183.72 ms` | `97.37%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `19.89 ms` | `44.13 ms` | `68.73 ms` | `97.37%` |
| **HuggingFace API** | `200 OK` | `34.88 ms` | `97.33 ms` | `149.24 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `46.73 ms` | `217.03 ms` | `288.47 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1795014980)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
