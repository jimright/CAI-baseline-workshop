# Module 1: Complete ML Workflow

Build a complete machine learning pipeline from data ingestion through model deployment and batch inference on Cloudera AI.

## Scripts

| Step | File | Purpose |
|------|------|---------|
| 1 | `01_ingest.py` | Load UCI Bank Marketing data into the data lake |
| 2 | `02_eda_notebook.ipynb` | Exploratory data analysis |
| 3 | `03_train_quick.py` | Train models with MLflow experiment tracking |
| 3+ | `03_train_extended.py` | Extended training with additional model types |
| 4 | `04_deploy.py` | Deploy best model as a REST API endpoint |
| 5a | `05.1_inference_data_prep.py` | Feature engineering for inference data |
| 5b | `05.2_inference_predict.py` | Generate predictions via deployed model |
| 6 | `06_Inference_101.ipynb` | Interactive inference walkthrough |

## Key Concepts

- MLflow experiment tracking and model registry
- Feature engineering pipelines (training/inference consistency)
- CML model deployment and API endpoints
- Job orchestration with dependencies

## Configuration

Update `shared_utils/config.py` with your deployed model endpoint and access key after Step 4.

## Lab Guide

For detailed step-by-step instructions, refer to the **Hands-on Lab Guide**.
