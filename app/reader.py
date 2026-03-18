from __future__ import annotations

import csv
from pathlib import Path
from typing import Any, Iterable, Mapping

Row = Mapping[str, Any]


def read_rows(files: list[str]) -> list[Row]:
    rows: list[Row] = []
    for path_str in files:
        path = Path(path_str)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        if not path.is_file():
            raise FileNotFoundError(f"Not a file: {path}")
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows.extend(reader)
    return rows
