# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-24 17:06:37 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `114.59 ms` | `93.04 ms` | `182.65 ms` | `97.73%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `31.34 ms` | `42.06 ms` | `67.93 ms` | `97.73%` |
| **HuggingFace API** | `200 OK` | `84.3 ms` | `96.22 ms` | `148.39 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `134.74 ms` | `212.53 ms` | `362.14 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1795539998)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
