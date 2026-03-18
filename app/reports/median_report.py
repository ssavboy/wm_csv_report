from __future__ import annotations

from collections import defaultdict
from statistics import median
from typing import Any, Iterable, Mapping

from .base import Report

Row = Mapping[str, Any]


class MedianCoffeReport(Report):
    def run(self, rows: Iterable[Row]) -> list[dict[str, Any]]:
        by_student: dict[str, list[float]] = defaultdict(list)

        for row in rows:
            name = row.get("student")
            spent_raw = row.get("coffee_spent")
            if name is None or spent_raw is None:
                continue
            spent = float(spent_raw)
            by_student[name].append(spent)

        result: list[dict[str, Any]] = []
        for student, spends in by_student.items():
            if not spends:
                continue
            result.append(
                {
                    "student": student,
                    "median_coffee": median(spends),
                }
            )

        result.sort(key=lambda r: r["median_coffee"], reverse=True)
        return result
