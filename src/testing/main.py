from src.parser.parse_sar_log import parse_sar_log
from src.testing.get_column_name import get_column_name
from src.testing.get_function_name import get_function_name
from src.testing.get_operator import get_operator
from src.testing.get_expected_value import get_expected_value
from src.testing.get_result import get_result
from src.testing.get_passed import get_passed
import json

def run_test(log_file, test_json_file, output_file=None):
    df = parse_sar_log(log_file)
    
    with open(test_json_file, 'r') as file:
        tests = json.load(file)
    
    # Check if the tests is a dictionary
    if not isinstance(tests, dict):
        raise ValueError("Invalid tests; Must be a dictionary")
    
    """
        * The 1. key in the JSON file is the name of the test.
        * The 2. key in the JSON file is the column name in the DataFrame.
        * The 3. key in the JSON file is the statistical function to apply.
        * The 4. key in the JSON file is the comparison operator.
    
        {
            "User mean must be less than 1": { 
                "user": { "mean": { "<": 1 } }
            },
            "Nice median must be greater than 1": { 
                "nice": { "median": { ">": 1 } }
            },
            "System max must equal 1": { 
                "system": { "max": { "=": 1 } }
            },
            "iowait mean must be greater than or equal to 1": { 
                "iowait": { "mean": { ">=": 1 } }
            },
            "steal min must be less than or equal to 1": { 
                "steal": { "min": { "<=": 1 } }
            },
            "idle sum must not equal 1": {
                "idle": { "sum": { "!=": 1 } }
            }
        }
    """
    
    results = []
    
    # Iterate over each test
    for test_name, test in tests.items():
        column_name = get_column_name(test, test_name)
        function_name = get_function_name(test, column_name, test_name)
        operator = get_operator(test, column_name, function_name, test_name)
        expected_value = get_expected_value(test, column_name, function_name, operator, test_name)
        result = get_result(df, column_name, function_name, test_name)
        passed = get_passed(operator, result, expected_value)
        
        results.append({
            "test_name": test_name,
            "passed": bool(passed),
            "result": result,
            "operator": operator,
            "expected_value": expected_value
        })
        
    for result in results:
        print(f"{result['test_name']}: {result['passed']} (Result: {result['result']}, Operator: {result['operator']}, Expected Value: {result['expected_value']})")
    
    if output_file:
        with open(output_file, 'w') as file:
            json.dump(results, file, indent=4)