from __future__ import annotations

import argparse
import sys
from typing import Sequence

from tabulate import tabulate

from .reader import read_rows
from .reports import REPORTS


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Создает отчеты о потреблении кофе студентами."
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Пути к CSV-файлам с данными о подготовке к экзамену.",
    )
    parser.add_argument(
        "--report", required=True, help="Название отчета (например, 'median-coffee')."
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)

    if args.report not in REPORTS:
        print(f"Неизвестный отчет: {args.report}", file=sys.stderr)
        print(f"Доступные отчеты: {', '.join(sorted(REPORTS))}", file=sys.stderr)
        raise SystemExit(1)

    try:
        rows = read_rows(args.files)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)

    report_cls = REPORTS[args.report]
    report = report_cls()
    data = report.run(rows)

    table = [[row["student"], row["median_coffee"]] for row in data]
    print(
        tabulate(
            table,
            headers=["student", "median_coffee"],
            tablefmt="github",
        )
    )


if __name__ == "__main__":
    main()
