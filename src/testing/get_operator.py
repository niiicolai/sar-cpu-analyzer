

def get_operator(test, column_name, function_name, test_name):
    valid_operators = ['<', '>', '=', '>=', '<=', '!=']
    
    # Check if test_name is a string
    if not isinstance(test_name, str):
        raise ValueError(f"Invalid test name: {test_name}; test_name must be a string")
    
    # Check if test[column_name][function_name] is a dictionary
    if not isinstance(test[column_name][function_name], dict):
        raise ValueError(f"Invalid test: {test_name}; The 3. key of a test must be a dictionary")
    
    # Check if test[column_name][function_name] have exactly one key
    if len(test[column_name][function_name].keys()) != 1:
            raise ValueError(f"Invalid test: {test_name}; The 3. key of a test must have exactly one key")
        
    operator = list(test[column_name][function_name].keys())[0]
    
    # Check if the operator is valid
    if operator not in valid_operators:
        raise ValueError(f"Invalid operator: {operator}; The 3. key of a test must be one of {valid_operators}")
    
    return operator
