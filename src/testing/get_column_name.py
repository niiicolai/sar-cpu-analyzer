

def get_column_name(test, test_name):
    valid_columns = ['%User', '%Nice', '%System', '%IOWait', '%Steal', '%Idle']
    
    if test is None:
        raise ValueError(f"Invalid test: {test_name}; The 1. key of a test must be a dictionary")
    if test_name is None:
        raise ValueError(f"Invalid test name: {test_name}; test_name must be a string")
    
    # Check if test_name is a string
    if not isinstance(test_name, str):
        raise ValueError(f"Invalid test name: {test_name}; test_name must be a string")
    
    # Check if test is a dictionary
    if not isinstance(test, dict):
        raise ValueError(f"Invalid test: {test_name}; The 1. key of a test must be a dictionary")
    
    # Check if test have exactly one key
    if len(test.keys()) != 1:
            raise ValueError(f"Invalid test: {test_name}; The 1. key of a test must have exactly one key")
        
    column_name = list(test.keys())[0]
        
    # Check if the column name is valid
    if column_name not in valid_columns:
        raise ValueError(f"Invalid column name: {column_name}; The 1. key of a test must be one of {valid_columns}")
                
    return column_name
