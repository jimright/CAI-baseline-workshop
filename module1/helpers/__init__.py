# Copyright 2026 Cloudera, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Helpers package for Module 1

Contains utility modules:
- preprocessing: Feature engineering and preprocessing pipelines
- _training_utils: Shared training utilities for MLflow
- utils: General utility functions
- test_runner: Automated test runner for sequential script execution
"""

# Core preprocessing imports (always available)
from .preprocessing import FeatureEngineer, PreprocessingPipeline, preprocess_for_training, split_data

# Training utilities (optional - requires mlflow and dependencies)
# These may not be available in minimal inference environments
try:
    from ._training_utils import setup_mlflow, train_model, calculate_metrics, apply_smote, save_results, print_summary
    _training_utils_available = True
except ImportError as e:
    # Training utilities not available (missing mlflow, pydantic, etc.)
    # This is fine for inference-only environments
    _training_utils_available = False
    setup_mlflow = train_model = calculate_metrics = apply_smote = save_results = print_summary = None

# General utilities
from .utils import engineer_customer_engagement_score, engineer_features, calculate_feature_importance_summary

# Test runner
try:
    from .test_runner import TestRunner
    _test_runner_available = True
except ImportError:
    _test_runner_available = False
    TestRunner = None

__all__ = [
    'FeatureEngineer',
    'PreprocessingPipeline',
    'preprocess_for_training',
    'split_data',
    'setup_mlflow',
    'train_model',
    'calculate_metrics',
    'apply_smote',
    'save_results',
    'print_summary',
    'engineer_customer_engagement_score',
    'engineer_features',
    'calculate_feature_importance_summary',
    'TestRunner',
]
