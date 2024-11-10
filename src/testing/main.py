from src.parser.parse_sar_log import parse_sar_log
from src.testing.get_column_name import get_column_name
from src.testing.get_function_name import get_function_name
from src.testing.get_operator import get_operator
from src.testing.get_expected_value import get_expected_value
from src.testing.get_result import get_result
from src.testing.get_passed import get_passed
import json

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
CYAN = "\033[96m"

def run_test(log_file, test_json_file, output_file=None, ignore_end_lines=0):
    df = parse_sar_log(log_file, ignore_end_lines)
    
    with open(test_json_file, 'r') as file:
        tests = json.load(file)
    
    # Check if the tests is a dictionary
    if not isinstance(tests, dict):
        raise ValueError("Invalid tests; Must be a dictionary")
    
    results = []
    
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

    # Print title
    print(f"\n{'='*30}")
    print(f"{'SAR Log Testing Results':^30}")
    print(f"{'='*30}")

    # Print the results of each test
    for result in results:
        print(f"\n\nTest Name: {result['test_name']}")
        print(f"Result: {result['result']}")
        print(f"Operator: {result['operator']}")
        print(f"Expected: {result['expected_value']}")
        print(f"Condition: {result['result']} {result['operator']} {result['expected_value']};")
        print(f"Passed: {f'{GREEN}True{RESET}' if result['passed'] else f'{RED}False{RESET}'}")
    
    total_passed = sum([result["passed"] for result in results])
    total_failed = len(results) - total_passed
    total_tests = len(results)
    all_passed = all([result["passed"] for result in results])
    
    # Print the summary as shown above
    print(f"\n\n| Total Passed | Total Failed | Total Tests |")
    print(f"|--------------|--------------|-------------|")
    print(f"| {GREEN}{total_passed}{RESET}            | {RED}{total_failed}{RESET}            | {CYAN}{total_tests}{RESET}           |")
    print(f"|--------------|--------------|-------------|")
    
    print(f"\n{f'{GREEN}Test Passed{RESET}' if all_passed else f'{RED}Test Failed{RESET}'}\n")

    
    if output_file:
        with open(output_file, 'w') as file:
            json.dump(results, file, indent=4)
        print(f"Test results saved to: {output_file}")
    
    return all_passed
