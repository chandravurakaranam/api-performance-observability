# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-10-28 12:18:45 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `186.36 ms` | `119.21 ms` | `183.88 ms` | `94.12%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `66.25 ms` | `49.69 ms` | `72.11 ms` | `94.12%` |
| **HuggingFace API** | `200 OK` | `113.05 ms` | `105.06 ms` | `142.45 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `203.72 ms` | `333.41 ms` | `840.15 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1793189926)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
