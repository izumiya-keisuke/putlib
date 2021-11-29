"""
Copyright 2021 Keisuke Izumiya

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import datetime as dt
from logging import getLogger, Logger
from pathlib import Path
from typing import Union


_logger = getLogger(__name__)


def convert_to_path(path: Union[Path, str]) -> Path:
    if isinstance(path, str):
        return Path(path)
    if isinstance(path, Path):
        return path

    _logger.error("`path` must be pathlib.Path or str, but got type=`%s`.", type(path))
    raise ValueError


def get_time_dir(root_path: Union[Path, str]) -> Path:
    return convert_to_path(root_path) / dt.datetime.now().strftime("%Y%m%d-%H%M%S")
