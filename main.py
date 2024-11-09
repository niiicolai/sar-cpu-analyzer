from src.report.main import generate_html_report
from src.testing.main import run_test
import argparse
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Analyze or test a SAR log file.")
    parser.add_argument('-i', type=str, required=True, help="The name and path to the log file")    
    parser.add_argument('-r', type=str, required=False, help="The name and path of the output HTML file with the report")
    parser.add_argument('-t', type=str, required=False, help="The name and path of the JSON file with the tests")
    parser.add_argument('-j', type=str, required=False, help="The name and path of the output JSON file with test results")
    args = parser.parse_args()
    
    if args.r:
        generate_html_report(args.r, args.i)
        print(f"HTML report generated: {args.r}")
        
    if args.t and not args.j:
        print("Error: -t (test file) provided without -j (output file)")
        exit()
        
    if args.j and not args.t:
        print("Error: -j (output file) provided without -t (test file)")
        exit()
        
    if args.t and args.j:
        run_test(args.i, args.t, args.j)
        print(f"Test results saved to: {args.j}")
