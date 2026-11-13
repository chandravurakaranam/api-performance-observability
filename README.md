# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-13 14:06:03 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `22.75 ms` | `100.34 ms` | `184.5 ms` | `96.97%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `18.85 ms` | `45.78 ms` | `68.38 ms` | `96.97%` |
| **HuggingFace API** | `200 OK` | `53.3 ms` | `99.62 ms` | `149.43 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `43.37 ms` | `236.08 ms` | `328.37 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1794578764)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
