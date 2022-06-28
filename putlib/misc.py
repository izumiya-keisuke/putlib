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

import os
from pathlib import Path
from tempfile import TemporaryDirectory


class Chdir:
    def __init__(self, path: Path) -> None:
        self._original_path: Path = Path.cwd()
        self._new_path: Path = path

    def __enter__(self) -> None:
        os.chdir(self._new_path)

    def __exit__(self, _0: any, _1: any, _2: any) -> None:
        os.chdir(self._original_path)


class TmpDir:
    def __init__(self) -> None:
        self._tmp_dir: TemporaryDirectory = TemporaryDirectory()
        self.path: Path = Path(self._tmp_dir.name)

    def __del__(self) -> None:
        self._cleanup()

    def __enter__(self) -> Path:
        return self.path

    def __exit__(self, _0: any, _1: any, _2: any) -> None:
        self._cleanup()

    def _cleanup(self) -> None:
        self._tmp_dir.cleanup()


def id_fn(x: any) -> any:
    return x


def range1(end: int, step: int = 1) -> range:
    return range(1, end + 1, step)
