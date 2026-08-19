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
Data lake connection utilities for Cloudera AI
Handles both Spark and direct Iceberg table access
"""

import os
import cml.data_v1 as cmldata
from pyspark.sql import SparkSession

def get_spark_session():
    """
    Initialize and return a Spark session configured for CML
    """
    spark = SparkSession.builder \
        .appName("MLOps Workshop") \
        .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog") \
        .config("spark.sql.catalog.spark_catalog.type", "hive") \
        .getOrCreate()
    
    return spark


def get_data_connection():
    """
    Get the CML data connection
    Supports both Spark-based and direct access
    """
    connection_name = os.getenv("DATA_LAKE_NAME", "go01-demo")
    conn = cmldata.get_connection(connection_name)
    return conn

    
def read_table_with_spark(database_name, table_name):
    """
    Read an Iceberg table using Spark
    
    Args:
        database_name: Name of the database
        table_name: Name of the table
        
    Returns:
        Spark DataFrame
    """
    spark = get_spark_session()
    full_table_name = f"{database_name}.{table_name}"
    df = spark.table(full_table_name)
    return df


def spark_to_pandas(spark_df):
    """
    Convert Spark DataFrame to Pandas with proper handling
    
    Args:
        spark_df: Spark DataFrame
        
    Returns:
        Pandas DataFrame
    """
    return spark_df.toPandas()