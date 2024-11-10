import pytest
import re
from src.testing.get_column_name import get_column_name

@pytest.mark.parametrize("test, test_name, expected", [
    ({"%User": 1}, "test", "%User"),
    ({"%Nice": 1}, "test", "%Nice"),
    ({"%System": 1}, "test", "%System"),
    ({"%IOWait": 1}, "test", "%IOWait"),
    ({"%Steal": 1}, "test", "%Steal"),
    ({"%Idle": 1}, "test", "%Idle")
])
def test_get_column_name_with_valid_partitions(test, test_name, expected):
    assert get_column_name(test, test_name) == expected
    
@pytest.mark.parametrize("test, test_name, expected", [
    ({"%User": 1}, 1, "Invalid test name: 1; test_name must be a string"),
    ({"%Nice": 1}, None, "Invalid test name: None; test_name must be a string"),
    ({"%System": 1}, 1.1, "Invalid test name: 1.1; test_name must be a string"),
    ({"%IOWait": 1}, [1], "Invalid test name: [1]; test_name must be a string"),
    ({"%Steal": 1}, {"test": 1}, "Invalid test name: {'test': 1}; test_name must be a string"),
    ({"%Idle": 1}, True, "Invalid test name: True; test_name must be a string"),
    (None, "test", "Invalid test: test; The 1. key of a test must be a dictionary"),
    ([1], "test", "Invalid test: test; The 1. key of a test must be a dictionary"),
    ({"invalid_column": 1}, "test", "Invalid column name: invalid_column; The 1. key of a test must be one of ['%User', '%Nice', '%System', '%IOWait', '%Steal', '%Idle']"),
])
def test_get_column_name_with_invalid_partitions(test, test_name, expected):
    with pytest.raises(ValueError, match=re.escape(expected)):
        get_column_name(test, test_name)
