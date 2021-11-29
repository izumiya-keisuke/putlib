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

from abc import abstractmethod, ABC
from multiprocessing import Process as OriginalProcess
from typing import Literal, Optional


class ProcessTarget(ABC):
    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def end_process(self) -> None:
        raise NotImplementedError


class Process(OriginalProcess):
    def __init__(
        self,
        group: Literal[None] = None,
        target: Optional[ProcessTarget] = None,
        name: Optional[str] = None,
        args: Optional[tuple[any, ...]] = None,
        kwargs: Optional[dict[any, any]] = None,
        *,
        daemon: Optional[bool] = None,
    ) -> None:
        super().__init__(target=target.run, name=name, args=args, kwargs=kwargs, daemon=daemon)

        self._target_instance: ProcessTarget = target_instance

    def terminate(self) -> None:
        self._target_instance.end_process()
        super().terminate()

    def kill(self) -> None:
        self._target_instance.end_process()
        super().kill()
