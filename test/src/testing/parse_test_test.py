import pytest
import re
from src.testing.parse_test import parse_test

@pytest.mark.parametrize("test, expected", [
    ({"%User": {"count": {"<": 1}}}, ("%User", "count", "<", 1)),
    ({"%Nice": {"median": {">": 1.1}}}, ("%Nice", "median", ">", 1.1)),
    ({"%System": {"mean": {"=": 1.1}}}, ("%System", "mean", "=", 1.1)),
    ({"%IOWait": {"max": {">=": 1.1}}}, ("%IOWait", "max", ">=", 1.1)),
    ({"%Steal": {"min": {"<=": 1.1}}}, ("%Steal", "min", "<=", 1.1)),
    ({"%Idle": {"sum": {"!=": 1.1}}}, ("%Idle", "sum", "!=", 1.1))
])
def test_parse_test_with_valid_partitions(test, expected):
    column_name, function_name, operator, expected_value = parse_test(test)
    assert column_name == expected[0]
    assert function_name == expected[1]
    assert operator == expected[2]
    assert expected_value == expected[3]

@pytest.mark.parametrize("test, expected", [
    (None, "Invalid test: None; The 1. key of a test must be a dictionary"),
    ([1], "Invalid test: [1]; The 1. key of a test must be a dictionary"),
    ({"%Invalid": {"count": {"<": 1}}}, "Invalid column name: %Invalid; The 1. key of a test must be one of ['%User', '%Nice', '%System', '%IOWait', '%Steal', '%Idle']"),
    ({"%User": None}, "Invalid test: {'%User': None}; The 2. key of a test must be a dictionary"),
    ({"%User": [1]}, "Invalid test: {'%User': [1]}; The 2. key of a test must be a dictionary"),
    ({"%User": {"invalid": {"<": 1}}}, "Invalid function name: invalid; The 2. key of a test must be one of ['count', 'median', 'mean', 'max', 'min', 'sum']"),
    ({"%User": {"count": None}}, "Invalid test: {'%User': {'count': None}}; The 3. key of a test must be a dictionary"),
    ({"%User": {"count": {"invalid": 1}}}, "Invalid operator: invalid; The 3. key of a test must be one of ['<', '>', '=', '>=', '<=', '!=']"),
    ({"%User": {"count": {"<": "invalid"}}}, "Invalid test: {'%User': {'count': {'<': 'invalid'}}}; The 4. key of a test must be a number"),
])
def test_parse_test_with_invalid_partitions(test, expected):
    with pytest.raises(ValueError, match=re.escape(expected)):
        parse_test(test)
        