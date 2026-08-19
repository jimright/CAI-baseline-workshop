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

"""Check all registered models across all projects"""
import cmlapi

cml_client = cmlapi.default_client()
models = cml_client.list_registered_models()

print(f"Total registered models: {len(models.models)}\n")

for i, model in enumerate(models.models, 1):
    print(f"{i}. {model.name}")
    print(f"   ID: {model.model_id}")
    print(f"   Project ID: {model.project_id if hasattr(model, 'project_id') else 'N/A'}")
    print(f"   Created: {model.created_at if hasattr(model, 'created_at') else 'N/A'}")

    # Check for our model
    if 'banking' in model.name.lower() or 'campaign' in model.name.lower():
        print(f"   ⭐ POSSIBLE MATCH!")
    print()
