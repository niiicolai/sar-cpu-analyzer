import pandas as pd

def get_result(df, column_name, function_name, test_name):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError(f"Invalid DataFrame: {df}; df must be a pandas DataFrame")
    
    # Check if column_name is a string
    if not isinstance(column_name, str):
        raise ValueError(f"Invalid column name: {column_name}; column_name must be a string")
    
    # Check if function_name is a string
    if not isinstance(function_name, str):
        raise ValueError(f"Invalid function name: {function_name}; function_name must be a string")
    
    # Check if test_name is a string
    if not isinstance(test_name, str):
        raise ValueError(f"Invalid test name: {test_name}; test_name must be a string")
    
    if function_name == "count":
        return df[column_name].count()
    elif function_name == "median":
        return df[column_name].median()
    elif function_name == "mean":
        return df[column_name].mean()
    elif function_name == "max":
        return df[column_name].max()
    elif function_name == "min":
        return df[column_name].min()
    elif function_name == "sum":
        return df[column_name].sum()
    else:
        raise ValueError(f"Invalid function name: {function_name}")
