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

from threading import Condition, Lock


class ReadWriteLock:
    def __init__(self) -> None:
        self._lock: Lock = Lock()
        self._cond: Condition = Condition(self._lock)

        self._reading_num: int = 0
        self._writing_num: int = 0
        self._waiting_writer_num: int = 0

        self._prefer_writer: bool = False

    def reader_acquire(self) -> None:
        with self._lock:
            while self._writing_num > 0 or (self._prefer_writer and self._waiting_writer_num > 0):
                self._cond.wait()

            self._reading_num += 1

    def reader_release(self) -> None:
        with self._lock:
            self._reading_num -= 1
            self._prefer_writer = True

            self._cond.notify_all()

    def writer_acquire(self) -> None:
        with self._lock:
            self._waiting_writer_num += 1
            while self._reading_num > 0 or self._writing_num > 0:
                self._cond.wait()

            self._waiting_writer_num -= 1
            self._writing_num += 1

    def writer_release(self) -> None:
        with self._lock:
            self._writing_num -= 1
            self._prefer_writer = False

            self._cond.notify_all()
