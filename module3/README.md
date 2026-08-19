# Module 3: Proactive MLOps — Drift Detection and Automated Retraining

Build an event-driven pipeline that proactively detects data drift and triggers automated retraining and deployment.

## Scripts

| File | Purpose |
|------|---------|
| `0_simulate_live_data.py` | Generate drifted production data |
| `1_check_drift.py` | Detect data drift using Evidently AI |
| `3_simulate_labeling_job.py` | Acquire labels for drifted data (triggered by drift status) |
| `4_retrain_model.py` | Retrain model on combined historical + new data |
| `5_register_and_deploy.py` | Register and deploy the retrained model |
| `reporting_launch_app.py` | CML Application to host drift report dashboard |
| `reporting_main_app.py` | Flask app serving the Evidently HTML report |

## Key Concepts

- Data drift detection with Evidently AI test suites
- Event-driven pipeline triggered by artifact creation (JSON status files)
- Automated model retraining and versioned deployment
- CML Applications for hosting visual reports

## Prerequisites

Complete Modules 1 and 2 (requires trained model and monitoring baseline).

## Lab Guide

For detailed step-by-step instructions, refer to the **Hands-on Lab Guide**.
