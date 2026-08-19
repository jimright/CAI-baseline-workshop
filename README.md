# MLOps Banking Lab

This project builds an end-to-end MLOps pipeline on Cloudera AI using a bank marketing prediction scenario. It demonstrates the complete ML lifecycle: training, deployment, monitoring, drift detection, automated retraining, and production inference with ONNX.

## Project Overview

- **Platform:** Cloudera AI (CML)
- **Dataset:** UCI Bank Marketing (binary classification — term deposit subscription)
- **Tools:** MLflow, Evidently AI, scikit-learn, ONNX Runtime

## Modules

| Module | Description |
|--------|-------------|
| [Module 1](./module1/) | Complete ML workflow — ingest, train, deploy, inference |
| [Module 2](./module2/) | Model monitoring with degradation detection |
| [Module 3](./module3/) | Proactive MLOps — drift detection and automated retraining |
| [Module 4](./module4/) | ONNX conversion and AI Inference Service deployment |

## Initialize the Project

**Prerequisites:**
- Cloudera AI workspace with Python 3.10+ runtime
- Spark 3.3.0 addon enabled

**Bootstrap:**

The project runs the `shared_utils/install-dependencies.py` script on initial setup to install required packages.

Set the `CONNECTION_NAME` environment variable to your data lake connection.

## Hands-on Lab Guide

For detailed step-by-step instructions, screenshots, and troubleshooting, refer to the separate **Hands-on Lab Guide** provided by your instructor.

## License

```
Copyright 2026 Cloudera, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
