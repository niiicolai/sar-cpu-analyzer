import pytest
import re
from src.testing.get_passed import get_passed

@pytest.mark.parametrize("operator, result, expected_value, expected", [
    ("<", 1, 2, True),
    (">", 2, 1, True),
    ("=", 1, 1, True),
    (">=", 2, 1, True),
    ("<=", 1, 2, True),
    ("!=", 1, 2, True),
    ("<", 2, 1, False),
    (">", 1, 2, False),
    ("=", 1, 2, False),
    (">=", 1, 2, False),
    ("<=", 2, 1, False),
    ("!=", 2, 2, False),
])
def test_get_passed_with_valid_partitions(operator, result, expected_value, expected):
    assert get_passed(operator, result, expected_value) == expected
    
@pytest.mark.parametrize("operator, result, expected_value, expected", [
    (None, 1, 2, "Invalid operator: None; operator must be a string"),
    (1, 1, 2, "Invalid operator: 1; operator must be a string"),
    ("invalid_operator", 1, 2, "Invalid operator: invalid_operator"),
    ("<", None, 2, "Invalid result: None; result must be a number"),
    ("<", "1", 2, "Invalid result: 1; result must be a number"),
    ("<", 1, None, "Invalid expected value: None; expected_value must be a number"),
    ("<", 1, "2", "Invalid expected value: 2; expected_value must be a number")
])
def test_get_passed_with_invalid_partitions(operator, result, expected_value, expected):
    with pytest.raises(ValueError, match=re.escape(expected)):
        get_passed(operator, result, expected_value)
