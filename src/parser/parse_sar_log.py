import pandas as pd

def parse_sar_log(log_file, ignore_end_lines=0):
    if not log_file:
        raise ValueError("No log file specified")
    if not isinstance(log_file, str):
        raise ValueError("Invalid log file; Must be a string")
    
    try:
        with open(log_file, 'r') as file:
            pass
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: '{log_file}'")
    
    data = []
    
    with open(log_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            fields = line.split()
            
            parsed_data = {}
            
            if len(fields) != 8:
                continue
            time, cpu, user, nice, system, iowait, steal, idle = fields                
            
            try:
                parsed_data = {
                    "Time": time,
                    "CPU": cpu,
                    "%User": float(user),
                    "%Nice": float(nice),
                    "%System": float(system),
                    "%IOWait": float(iowait),
                    "%Steal": float(steal),
                    "%Idle": float(idle),
                }
                data.append(parsed_data)
            except ValueError:
                pass
    
    if len(data) == 0:
        raise ValueError(f"The parser could not find any valid lines: {log_file}; Ensure the file contains time, cpu, user, nice, system, iowait, steal, and idle fields. Also ensure it is not empty.")
    
    df = pd.DataFrame(data)
    
    if ignore_end_lines:
        if isinstance(ignore_end_lines, bool):
            raise ValueError("Invalid ignore_end_lines; Must be an integer")
        if not isinstance(ignore_end_lines, int):
            raise ValueError("Invalid ignore_end_lines; Must be an integer")
        if ignore_end_lines < 0:
            raise ValueError("Invalid ignore_end_lines; Must be greater than or equal to 0")
        if ignore_end_lines >= len(df):
            raise ValueError("Invalid ignore_end_lines; Must be less than the number of lines in the log file")
        df = df.iloc[:-ignore_end_lines]   
    
    return df
