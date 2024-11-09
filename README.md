# SAR CPU HTML Report Generator
A python script to generate a HTML report from SAR CPU data.

## Example CPU Data
```bash
Linux 6.11.0-9-generic (ubuntu-s-1vcpu-2gb-ams3-01)     11/09/24        _x86_64_        (1 CPU)

00:33:53        CPU     %user     %nice   %system   %iowait    %steal     %idle
00:33:55        all      2.01      0.00      0.50      0.50      0.00     96.98
00:33:57        all      1.52      0.00      1.01      0.00      0.51     96.97
00:33:59        all      2.53      0.00      1.52      0.00      0.00     95.96
00:34:01        all      2.50      0.00      1.00      0.00      2.00     94.50
00:34:03        all      2.45      0.00      1.47      0.00      3.92     92.16
00:34:05        all      2.51      0.00      1.51      0.00      0.00     95.98
00:34:07        all      2.51      0.00      1.51      0.00      0.00     95.98
00:34:09        all      2.02      0.00      1.01      0.51      0.51     95.96
00:34:11        all      2.04      0.00      1.02      0.00      0.00     96.94
00:34:13        all      2.51      0.00      1.51      0.00      0.00     95.98
00:34:15        all      2.53      0.00      0.51      0.00      0.51     96.46
00:34:17        all      2.51      0.00      1.51      0.00      0.00     95.98
00:34:19        all      2.02      0.00      1.52      4.04      0.00     92.42
00:34:21        all      2.02      0.00      1.52      0.00      0.51     95.96
00:34:23        all      0.51      0.00      0.51      0.00      0.00     98.99
```

## Setup
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate 2>/dev/null || venv\Scripts\activate 2>/dev/null || source venv/Scripts/activate 2>/dev/null && echo "Virtual environment activated." || echo "Failed to activate virtual environment."

# Install the dependencies
pip install -r requirements.txt
```

## Usage
```bash
# Generate the HTML report
python main.py -i <input_file> -o <output_file>

# Help
python main.py --help
```

## Example
```bash
python main.py -i data.txt -o report.html
```
