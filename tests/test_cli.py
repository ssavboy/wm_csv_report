import pytest

from app.cli import main


def test_main_unknown_report_exits_with_error(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["--files", "dummy.csv", "--report", "unknown"])

    assert exc.value.code == 1
    captured = capsys.readouterr()
    assert "Неизвестный отчет" in captured.err
