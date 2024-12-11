# Copyright 2023-2024 PKU-Alignment Team. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
# This file is modified from:
# https://github.com/PKU-Alignment/safe-rlhf/safe_rlhf/values/__init__.py
# ==============================================================================
"""Value models for Safe-RLHF."""

from safe_rlhf.values.cost import CostTrainer
from safe_rlhf.values.reward import RewardTrainer


__all__ = ['RewardTrainer', 'CostTrainer']