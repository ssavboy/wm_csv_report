from app.reader import read_rows


def test_read_rows_reads_all_files(tmp_path):
    csv1 = tmp_path / "file1.csv"
    csv1.write_text(
        "student,date,coffee_spent\n" "Alice,2024-06-01,100\n",
        encoding="utf-8",
    )
    csv2 = tmp_path / "file2.csv"
    csv2.write_text(
        "student,date,coffee_spent\n" "Bob,2024-06-01,200\n",
        encoding="utf-8",
    )

    rows = read_rows([str(csv1), str(csv2)])

    assert len(rows) == 2
    assert rows[0]["student"] == "Alice"
    assert rows[1]["student"] == "Bob"
