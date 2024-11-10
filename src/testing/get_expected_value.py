

def get_expected_value(test, column_name, function_name, operator, test_name):
    # Check if test_name is a string
    if not isinstance(test_name, str):
        raise ValueError(f"Invalid test name: {test_name}; test_name must be a string")
    
    # Check if test[column_name][function_name][operator] is a number
    if not isinstance(test[column_name][function_name][operator], (int, float)):
        raise ValueError(f"Invalid test: {test_name}; The 4. key of a test must be a number")
        
    return test[column_name][function_name][operator]

    