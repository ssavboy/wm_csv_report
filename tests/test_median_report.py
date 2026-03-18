from app.reports.median_report import MedianCoffeReport


def test_median_coffee_report_calculates_and_sorts():
    rows = [
        {"student": "Alice", "coffee_spent": "100"},
        {"student": "Alice", "coffee_spent": "300"},
        {"student": "Bob", "coffee_spent": "200"},
        {"student": "Bob", "coffee_spent": "400"},
        {"student": "Bob", "coffee_spent": "600"},
    ]

    report = MedianCoffeReport()
    result = report.run(rows)

    assert result == [
        {"student": "Bob", "median_coffee": 400.0},
        {"student": "Alice", "median_coffee": 200.0},
    ]
