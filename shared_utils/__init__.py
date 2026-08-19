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
Shared utilities for MLOps workshop
"""

from .config import (
    DATALAKE_CONFIG,
    MODEL_CONFIG,
    FEATURE_CONFIG,
    API_CONFIG,
)

# Optional Spark imports - only load if pyspark is available
try:
    from .data_connection import (
        get_spark_session,
        get_data_connection,
        read_table_with_spark,
        spark_to_pandas
    #,    write_to_datalake_spark
    #,    append_to_datalake_spark,
    )
    _SPARK_AVAILABLE = True
except ImportError as e:
    # Only suppress pyspark import errors; re-raise other errors
    if "pyspark" not in str(e):
        raise
    _SPARK_AVAILABLE = False
    get_spark_session = None
    get_data_connection = None
    read_table_with_spark = None
    spark_to_pandas = None

__all__ = [
    # Config
    'DATALAKE_CONFIG',
    'MODEL_CONFIG',
    'FEATURE_CONFIG',
    'API_CONFIG',
    # Data connections
    'get_spark_session',
    'get_data_connection',
    'read_table_with_spark',
    'spark_to_pandas',
    'write_to_datalake_spark',
    'append_to_datalake_spark',
]