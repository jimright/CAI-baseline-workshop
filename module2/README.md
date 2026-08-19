# Module 2: Model Monitoring with Degradation Detection

Implement a monitoring pipeline that tracks model predictions over time and automatically detects accuracy degradation.

## Scripts

| File | Purpose |
|------|---------|
| `01_create_jobs.ipynb` | Create CML monitoring jobs programmatically |
| `02.1_job1_prepare_artificial_data.py` | Generate artificial ground truth with simulated degradation |
| `02.2_job2_monitoring_pipeline.py` | Integrated monitoring pipeline — processes all periods sequentially |
| `04_model_metrics_analysis.ipynb` | Diagnostics and visualization of degradation trends |

## Key Concepts

- Simulated model degradation across time periods
- Programmatic CML job creation via API
- Period-based accuracy monitoring with configurable thresholds
- CML metric tracking (`track_delayed_metrics`, `track_aggregate_metrics`)
- Automated alerting when accuracy drops below threshold

## Prerequisites

Complete Module 1 (requires trained model and inference data).

## Lab Guide

For detailed step-by-step instructions, refer to the **Hands-on Lab Guide**.
