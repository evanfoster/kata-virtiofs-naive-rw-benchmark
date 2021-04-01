#!/usr/bin/env python3
import argparse
import json
import time

from dataclasses import dataclass
from pathlib import Path
from typing import Union


@dataclass
class TestResult:
    start_time: float
    end_time: float
    megabytes: int

    @property
    def delta_t(self) -> float:
        return self.end_time - self.start_time

    @property
    def bandwidth(self) -> float:
        return f"{round(self.megabytes / self.delta_t, 4)} MB/s"

    def as_dict(self) -> dict[str, Union[int, float]]:
        return {"megs": self.megabytes, "throughput": self.bandwidth}


def test_write(megabytes: int, file_path: Path = Path("test_file.dat")) -> TestResult:
    chunk_size = 1024
    write_count = (megabytes * 1048576) / chunk_size
    data = bytearray(chunk_size)

    with open(file_path, mode="wb") as fd:
        start_time = time.time()
        while write_count >= 0:
            fd.write(data)
            write_count -= 1
    end_time = time.time()
    return TestResult(start_time, end_time, megabytes)


def test_read(file_path: Path = Path("test_file.dat")) -> TestResult:
    chunk_size = 64 * 1024  # copying node's createReadStream here
    data_length = 0
    with open(file_path, mode="rb") as fd:
        start_time = time.time()
        while data := fd.read(chunk_size):
            data_length += len(data)
        end_time = time.time()
    return TestResult(start_time, end_time, data_length / 1048576)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("megabytes", type=int)
    parser.add_argument("--test-path", "-f", type=Path, default=Path("test_file.dat"))
    args = parser.parse_args()
    megabytes: int = args.megabytes
    file_path: Path = args.test_path
    write_test_result = test_write(megabytes, file_path)
    read_test_result = test_read(file_path)
    print(
        json.dumps(
            {
                "done": True,
                "test": "disk",
                "write": write_test_result.as_dict(),
                "read": read_test_result.as_dict(),
            },
            sort_keys=True,
            indent=True,
        )
    )


if __name__ == "__main__":
    main()
