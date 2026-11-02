# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-02 14:59:14 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `105.13 ms` | `115.36 ms` | `186.2 ms` | `95.45%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `38.17 ms` | `47.74 ms` | `71.3 ms` | `95.45%` |
| **HuggingFace API** | `200 OK` | `79.83 ms` | `101.66 ms` | `141.53 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `68.45 ms` | `295.08 ms` | `415.9 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1793631555)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
