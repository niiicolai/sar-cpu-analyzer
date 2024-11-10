from src.report.main import generate_html_report
from src.testing.main import run_test
import argparse
import sys
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Analyze or test a SAR log file.")
    parser.add_argument('-i', type=str, required=True, help="Path to the SAR log file")    
    parser.add_argument('-r', type=str, required=False, help="Path for the HTML report output file")
    parser.add_argument('-t', type=str, required=False, help="Path to the JSON test specification file")
    parser.add_argument('-j', type=str, required=False, help="Path for the JSON test results output file")
    parser.add_argument('--ignore-end-lines', type=int, required=False, help="Specify a number of lines to ignore at the end of the log file")
    args = parser.parse_args()
    
    if args.r:
        generate_html_report(args.r, args.i, args.ignore_end_lines)
        print(f"HTML report generated: {args.r}")
        
    if args.i and args.t:
        if run_test(args.i, args.t, args.j, args.ignore_end_lines):                        
            sys.exit(0)
        else:
            print("Error: Test failed")
            sys.exit(1)
            
    if not args.r and not args.t and not args.j:
        print("Error: No action specified")
        sys.exit(1)
            
    sys.exit(0)            
