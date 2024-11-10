import pytest
import re
from src.testing.get_result import get_result
import pandas as pd

@pytest.mark.parametrize("df, column_name, function_name, test_name, expected", [
    (pd.DataFrame({"%User": [1, 2, 3]}), "%User", "count", "test", 3),
    (pd.DataFrame({"%User": [1, 2, 3]}), "%User", "median", "test", 2),
    (pd.DataFrame({"%User": [1, 2, 3]}), "%User", "mean", "test", 2),
    (pd.DataFrame({"%User": [1, 2, 3]}), "%User", "max", "test", 3),
    (pd.DataFrame({"%User": [1, 2, 3]}), "%User", "min", "test", 1),
    (pd.DataFrame({"%User": [1, 2, 3]}), "%User", "sum", "test", 6),
])
def test_get_result_with_valid_partitions(df, column_name, function_name, test_name, expected):
    assert get_result(df, column_name, function_name, test_name) == expected
    
@pytest.mark.parametrize("df, column_name, function_name, test_name, expected", [
    (None, "%User", "count", "test", "Invalid DataFrame: None; df must be a pandas DataFrame"),
    (1, "%User", "count", "test", "Invalid DataFrame: 1; df must be a pandas DataFrame"),
    (pd.DataFrame({"%User": [1, 2, 3]}), None, "count", "test", "Invalid column name: None; column_name must be a string"),
    (pd.DataFrame({"%User": [1, 2, 3]}), 1, "count", "test", "Invalid column name: 1; column_name must be a string"),
    (pd.DataFrame({"%User": [1, 2, 3]}), "%User", None, "test", "Invalid function name: None; function_name must be a string"),
    (pd.DataFrame({"%User": [1, 2, 3]}), "%User", 1, "test", "Invalid function name: 1; function_name must be a string"),
    (pd.DataFrame({"%User": [1, 2, 3]}), "%User", "count", None, "Invalid test name: None; test_name must be a string"),
    (pd.DataFrame({"%User": [1, 2, 3]}), "%User", "count", 1, "Invalid test name: 1; test_name must be a string"),
    (pd.DataFrame({"%User": [1, 2, 3]}), "%User", "invalid", "test", "Invalid function name: invalid"),
])
def test_get_result_with_invalid_partitions(df, column_name, function_name, test_name, expected):
    with pytest.raises(ValueError, match=re.escape(expected)):
        get_result(df, column_name, function_name, test_name)
