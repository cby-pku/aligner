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
# https://github.com/PKU-Alignment/safe_rlhf/datasets/raw/__init__.py
# ==============================================================================
"""Raw datasets."""

from training.datasets.raw.alpaca import AlpacaDataset
from training.datasets.raw.firefly import FireflyDataset
from training.datasets.raw.hh_rlhf import (
    HhRLHFDialogueDataset,
    HhRLHFHarmlessDialogueDataset,
    HhRLHFHelpfulDialogueDataset,
)
from training.datasets.raw.moss import MOSS002SFT, MOSS003SFT
from training.datasets.raw.safe_rlhf import (
    SafeRLHF10KTrainDataset,
    SafeRLHF30KTestDataset,
    SafeRLHF30KTrainDataset,
    SafeRLHFDataset,
    SafeRLHFTestDataset,
    SafeRLHFTrainDataset,
)


from training.datasets.raw.correction import (
    CorrectionJSONDataset,
    BeavertailsJSONDataset,
    BeavertailsTestJSONDataset,
    BeavertailsTrainJSONDataset,
)
from training.datasets.raw.empathy import (
    EmpathyJSONDataset
)
__all__ = [
    'AlpacaDataset',
    'FireflyDataset',
    'HhRLHFDialogueDataset',
    'HhRLHFHarmlessDialogueDataset',
    'HhRLHFHelpfulDialogueDataset',
    'MOSS002SFT',
    'MOSS003SFT',
    'SafeRLHFDataset',
    'SafeRLHFTrainDataset',
    'SafeRLHFTestDataset',
    'SafeRLHF30KTrainDataset',
    'SafeRLHF30KTestDataset',
    'SafeRLHF10KTrainDataset',
    'CorrectionJSONDataset',
    'BeavertailsJSONDataset',
    'BeavertailsTestJSONDataset',
    'BeavertailsTrainJSONDataset',
    'EmpathyJSONDataset',
]
