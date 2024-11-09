from parse_sar_log import parse_sar_log
from generate_html_report import generate_html_report
import argparse
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the generate html report function with a specified log file.")
    parser.add_argument('-i', type=str, required=True, help="The name and path to the log file")    
    parser.add_argument('-o', type=str, required=True, help="The name and path of the output file")
    
    args = parser.parse_args()
    
    df = parse_sar_log(args.i)
    generate_html_report(df, args.o, args.i)
    print(f"HTML report generated: {args.o}")
