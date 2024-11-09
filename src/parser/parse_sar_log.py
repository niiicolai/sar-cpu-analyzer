import pandas as pd

def parse_sar_log(log_file):
    data = []
    with open(log_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Ignore header and system info lines
            if line.startswith("Linux") or line.startswith("00:") is False:
                continue
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
    
    df = pd.DataFrame(data)
    return df
