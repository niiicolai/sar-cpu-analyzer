

def get_function_name(test, column_name, test_name):
    valid_functions = ['count', 'median', 'mean', 'max', 'min', 'sum']
    
    # Check if test_name is a string
    if not isinstance(test_name, str):
        raise ValueError(f"Invalid test name: {test_name}; test_name must be a string")
    
    # Check if test[column_name] is a dictionary
    if not isinstance(test[column_name], dict):
        raise ValueError(f"Invalid test: {test_name}; The 2. key of a test must be a dictionary")
    
    # Check if test[column_name] have exactly one key
    if len(test[column_name].keys()) != 1:
            raise ValueError(f"Invalid test: {test_name}; The 2. key of a test must have exactly one key")
        
    function_name = list(test[column_name].keys())[0]
    
    # Check if the function name is valid
    if function_name not in valid_functions:
        raise ValueError(f"Invalid function name: {function_name}; The 2. key of a test must be one of {valid_functions}")
                
    return function_name
