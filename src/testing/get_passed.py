
def get_passed(operator, result, expected_value):
    if operator is None: raise ValueError(f"Invalid operator: {operator}; operator must be a string")
    if not isinstance(operator, str): raise ValueError(f"Invalid operator: {operator}; operator must be a string")
    
    if result is None: raise ValueError(f"Invalid result: {result}; result must be a number")
    if not isinstance(result, (int, float)): raise ValueError(f"Invalid result: {result}; result must be a number")
    
    if expected_value is None: raise ValueError(f"Invalid expected value: {expected_value}; expected_value must be a number")
    if not isinstance(expected_value, (int, float)): raise ValueError(f"Invalid expected value: {expected_value}; expected_value must be a number")
    
    if operator == "<":
        return result < expected_value
    elif operator == ">":
        return result > expected_value
    elif operator == "=":
        return result == expected_value
    elif operator == ">=":
        return result >= expected_value
    elif operator == "<=":
        return result <= expected_value
    elif operator == "!=":
        return result != expected_value
    else:
        raise ValueError(f"Invalid operator: {operator}")
