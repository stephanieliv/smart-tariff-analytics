# ⚡ Smart Tariff Analytics  
*An end-to-end data engineering project aligned with AER’s Network Tariff Reform and Kraken Technologies’ mission to modernise energy systems.*

---

## 🌍 Overview  
**Smart Tariff Analytics** is a data engineering portfolio project built using **Databricks**, **dbt**, **AWS**, and **Python**.  
It automates the ingestion, transformation, and modelling of **Australian energy usage and tariff data** to explore how tariff design, solar generation, and battery availability influence grid demand and consumer costs.

This project aligns with the [AER Network Tariff Reform](https://www.aer.gov.au/about/strategic-initiatives/network-tariff-reform), promoting cost-reflective tariffs and smarter energy use to support Australia’s renewable transition.

---

## ⚙️ Tech Stack
**Core tools:**  
- Databricks (Delta Lake, PySpark)  
- dbt (Databricks adapter)  
- AWS S3 (data storage)  
- Python (API ingestion + analysis)  
- SQL (transformations)  
- GitHub Actions (CI/CD)

---

## 🧠 Objectives
- Build a reproducible data pipeline: *ingest → transform → model → visualise*  
- Demonstrate best practices in data engineering (dbt tests, CI, documentation)  
- Model energy demand and tariff impacts across NSW, QLD, SA, VIC  
- Explore renewable integration (solar & battery) in grid demand

---

## 🏗️ Architecture
OpenNEM API → Databricks Ingest → Delta Lake (raw/staging)
→ dbt Models → Analytics Marts → Forecasts + Visuals


---

## 📊 Deliverables
- Python API ingestion script (OpenNEM)
- Databricks Delta Lake staging & transformation
- dbt models and tests
- Forecasting and tariff simulation notebooks
- GitHub documentation & 5–8 minute walkthrough demo

---

## 🔜 Current Progress
- ✅ OpenNEM API key configured in Databricks  
- 🔄 Ingestion script in development  
- 🧱 Repo structure established and tracked via 10-day sprint plan  

---

## 👩‍💻 Author  
**Stephanie Livingstone** — Sydney, Australia  
Focused on sustainable energy analytics and data engineering.  
[LinkedIn](https://linkedin.com) | [GitHub](https://github.com/yourusername)

---

*Part of a two-week upskilling sprint to demonstrate full-stack data engineering workflow design for Kraken-style energy data systems.*
