# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-26 16:33:06 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `66.73 ms` | `91.86 ms` | `182.24 ms` | `97.83%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `18.9 ms` | `41.15 ms` | `67.74 ms` | `97.83%` |
| **HuggingFace API** | `200 OK` | `106.17 ms` | `95.95 ms` | `147.89 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `207.67 ms` | `210.07 ms` | `350.65 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1795710787)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
