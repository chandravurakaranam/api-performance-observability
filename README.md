# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-26 12:26:24 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `107.95 ms` | `110.46 ms` | `178.52 ms` | `93.33%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `71.57 ms` | `48.28 ms` | `72.37 ms` | `93.33%` |
| **HuggingFace API** | `200 OK` | `115.28 ms` | `104.94 ms` | `142.67 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `203.54 ms` | `346.98 ms` | `1048.16 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1793017585)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
