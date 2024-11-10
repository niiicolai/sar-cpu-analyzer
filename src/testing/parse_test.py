

def parse_test(test):
    valid_columns = ['%User', '%Nice', '%System', '%IOWait', '%Steal', '%Idle']
    valid_functions = ['count', 'median', 'mean', 'max', 'min', 'sum']
    valid_operators = ['<', '>', '=', '>=', '<=', '!=']
    
    if test is None:
        raise ValueError(f"Invalid test: {test}; The 1. key of a test must be a dictionary")
    
    if not isinstance(test, dict):
        raise ValueError(f"Invalid test: {test}; The 1. key of a test must be a dictionary")
    
    if len(test.keys()) != 1:
        raise ValueError(f"Invalid test: {test}; The 1. key of a test must have exactly one key")
    
    column_name = list(test.keys())[0]
    
    if column_name not in valid_columns:
        raise ValueError(f"Invalid column name: {column_name}; The 1. key of a test must be one of {valid_columns}")
    
    if not isinstance(test[column_name], dict):
        raise ValueError(f"Invalid test: {test}; The 2. key of a test must be a dictionary")
    
    if len(test[column_name].keys()) != 1:
        raise ValueError(f"Invalid test: {test}; The 2. key of a test must have exactly one key")
    
    function_name = list(test[column_name].keys())[0]
    
    if function_name not in valid_functions:
        raise ValueError(f"Invalid function name: {function_name}; The 2. key of a test must be one of {valid_functions}")
    
    if not isinstance(test[column_name][function_name], dict):
        raise ValueError(f"Invalid test: {test}; The 3. key of a test must be a dictionary")
    
    if len(test[column_name][function_name].keys()) != 1:
        raise ValueError(f"Invalid test: {test}; The 3. key of a test must have exactly one key")
    
    operator = list(test[column_name][function_name].keys())[0]
    
    if operator not in valid_operators:
        raise ValueError(f"Invalid operator: {operator}; The 3. key of a test must be one of {valid_operators}")
    
    if not isinstance(test[column_name][function_name][operator], (int, float)):
        raise ValueError(f"Invalid test: {test}; The 4. key of a test must be a number")
    
    expected_value = test[column_name][function_name][operator]
    
    return column_name, function_name, operator, expected_value

    