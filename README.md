# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-12 14:46:47 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `19.81 ms` | `102.77 ms` | `184.66 ms` | `96.88%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `21.71 ms` | `46.63 ms` | `68.64 ms` | `96.88%` |
| **HuggingFace API** | `200 OK` | `31.08 ms` | `101.07 ms` | `149.46 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `40.18 ms` | `242.11 ms` | `336.35 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1794494808)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
