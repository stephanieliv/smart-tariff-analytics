# ⚡ Smart Tariff Analytics — Project Scope Document

---

## 📘 Project Overview
Smart Tariff Analytics is a data engineering project designed to model the impact of tariff design and renewable availability on electricity demand across Australia.

Using the **OpenNEM API** and related tariff datasets, this project builds an automated data pipeline in **Databricks** (Delta Lake + dbt) to ingest, clean, transform, and model grid-level demand and tariff data for NSW, QLD, SA, and VIC.

The project aligns with the **AER’s Network Tariff Reform** initiative and demonstrates end-to-end data engineering workflow design consistent with **Kraken Technologies’** data platform principles.

---

## 🎯 Objectives & Scope

### In Scope
- Connect to OpenNEM API and ingest regional demand / generation data  
- Simulate or ingest tariff data for NSW, QLD, SA, VIC (residential + SME)  
- Create clean staging and analytical layers via dbt  
- Generate demand forecasts and tariff-cost simulations  
- Produce documentation and visuals for portfolio presentation  

### Out of Scope
- Advanced ML models (beyond baseline forecasting)  
- Real-time orchestration pipelines  
- Full production infrastructure (CI/CD, monitoring)

---

## 🧩 Architecture Summary
OpenNEM API → Databricks (raw/staging Delta)
→ dbt Models → Analytical Marts → Forecasts + Visuals


**Core Tools**
- Databricks (Delta Lake, PySpark, Jobs)  
- dbt (Databricks adapter, tests, docs)  
- Python (API ingestion, transformation, visualisation)  
- AWS S3 (data storage backend)  
- GitHub Actions (CI/CD)

---

## 📊 Data Sources & Dataset Links

| Dataset | Source | Description | Access Type |
|----------|---------|--------------|--------------|
| **OpenNEM API** | [https://opennem.org.au/](https://opennem.org.au/) | Energy generation & demand data (by fuel, region, timestamp) | API (awaiting authorisation) |
| **AER Tariff Data** | [AER Tariff Reform](https://www.aer.gov.au/about/strategic-initiatives/network-tariff-reform) | Tariff structures and pricing reform context | Web / Public |
| **AEMO Data Portal** | [AEMO Datasets](https://aemo.com.au/) | Regional demand and solar generation | Public download |
| **Synthetic Tariff Profiles** | Local CSVs | Simulated SME and residential usage patterns | Local (manual) |

*Once API access is authorised, exact endpoints will be added, e.g.*  
`https://api.opennem.org.au/v3/dispatch/regions`  
`https://api.opennem.org.au/v3/energy/regions`

---

## 🧱 Project Deliverables
- Databricks notebooks (ingestion, transformation, forecasting)  
- dbt models, schema tests & docs  
- Delta tables: raw, staging, analytics  
- Slide deck + demo walkthrough  
- GitHub documentation + README updates  

---

## 📆 Timeline & Milestones
| Phase | Focus | Duration |
|-------|--------|-----------|
| **Week 1** | Data ingestion, cleaning & staging setup | Days 1–5 |
| **Week 2** | Modelling, simulation & presentation prep | Days 6–10 |

Reference: [`docs/Smart_Tariff_Analytics_10Day_CompletePlan.xlsx`](Smart_Tariff_Analytics_10Day_CompletePlan.xlsx)

---

## 📈 Success Metrics
| Category | Metric | Target |
|-----------|---------|---------|
| Data Quality | Null value % < 1%, schema validated | ✅ |
| Pipeline Performance | dbt tests pass, runtime < 5 min | ✅ |
| Insights Accuracy | Forecast MAE < 10% | ✅ |
| Documentation | Clear instructions & reproducibility | ✅ |
| Visualisation | Dashboard refresh < 30 s & clarity | ✅ |

---

## 🔒 Risks & Assumptions
| Risk | Impact | Mitigation |
|------|---------|------------|
| API access delayed | Medium | Use cached or sample JSON for testing |
| Missing tariff data | High | Create synthetic tariff table with documented assumptions |
| Time limitations | Medium | Prioritise pipeline & dbt deliverables before visualisation |
| Data volume too large | Low | Use incremental ingestion and sampling |

---

*Document created for Smart Tariff Analytics — Kraken Technologies Application Project.*
