# 🌐 Automated Cloud API Observability & Benchmark Suite

*Automated test execution timestamp:* **2026-11-11 13:43:49 UTC**

An automated reliability and performance testing engine that monitors core tech infrastructure APIs, logs round-trip response latencies, tracks P95 response SLA degradation, and records data directly into Git.

## 📈 System SLA & Latency Performance Summary

| Service | Status | Current Latency | Avg Latency | P95 Latency | SLA Uptime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GitHub API** | `200 OK` | `110.35 ms` | `105.44 ms` | `184.81 ms` | `96.77%` |
| **Cloudflare DNS (1.1.1.1)** | `200 OK` | `51.14 ms` | `47.43 ms` | `68.91 ms` | `96.77%` |
| **HuggingFace API** | `200 OK` | `149.13 ms` | `103.33 ms` | `149.5 ms` | `100.0%` |
| **HTTPBin Echo** | `200 OK` | `159.78 ms` | `248.62 ms` | `344.33 ms` | `100.0%` |

### 📊 Historical Latency Trend
![Latency Trends](latency_trend.png?v=1794404630)

---

### 🗄️ Historical Dataset
All raw performance benchmarks are continuously logged to [`history.csv`](./history.csv) on every automated run.

---
*Built with Python (`requests`, `pandas`, `matplotlib`) and GitHub Actions.*
