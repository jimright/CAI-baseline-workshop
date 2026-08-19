# Module 4: Production Deployment with AI Inference Service

Convert a trained model to ONNX format and deploy to Cloudera AI Inference Service for production-grade serving.

## Scripts

| File | Purpose |
|------|---------|
| `01_create_onnx_model.py` | Train, convert to ONNX, and register in MLflow |
| `02_compare_endpoints.ipynb` | Compare CML Models vs AI Inference Service performance |

## Key Concepts

- sklearn to ONNX conversion for optimized inference
- MLflow Model Registry with versioning
- Cloudera AI Inference Service deployment (autoscaling, HA)
- Open Inference Protocol vs CML model endpoints
- Performance benchmarking (latency, throughput)

## Prerequisites

Complete Module 3 (requires retrained model and labeled data).

## Lab Guide

For detailed step-by-step instructions and UI deployment walkthrough, refer to the **Hands-on Lab Guide**.
