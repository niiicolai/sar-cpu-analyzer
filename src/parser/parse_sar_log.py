import pandas as pd

def parse_sar_log(log_file, ignore_end_lines=0):
    data = []
    with open(log_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            fields = line.split()
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
        raise ValueError(f"Empty log file: {log_file}")
    
    if ignore_end_lines:
        # Ensure ignore_end_lines is an integer
        if not isinstance(ignore_end_lines, int):
            raise ValueError("Invalid ignore_end_lines; Must be an integer")
        # ensure ignore_end_lines is less than the number of lines in the log file
        if ignore_end_lines >= len(df):
            raise ValueError("Invalid ignore_end_lines; Must be less than the number of lines in the log file")
        df = df.iloc[:-ignore_end_lines]   
    
    df = pd.DataFrame(data)
    return df
