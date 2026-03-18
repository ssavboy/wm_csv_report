from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Iterable, Mapping

Row = Mapping[str, Any]


class Report(ABC):
    @abstractmethod
    def run(self, rows: Iterable[Row]) -> list[dict[str, Any]]:
        """Выполнить отчет и вернуть список строк результата."""
        raise NotImplementedError
