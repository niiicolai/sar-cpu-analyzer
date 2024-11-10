from datetime import datetime
from src.report.generate_collapse_div import generate_collapse_div
from src.report.generate_line_chart import generate_line_chart
from src.report.generate_table import generate_table
from src.parser.parse_sar_log import parse_sar_log

def generate_html_report(output, log_file, ignore_end_lines=0):
    df = parse_sar_log(log_file, ignore_end_lines)
    
    style = """
        <style>
            body { padding: 20px; }
            canvas { width: 100%; }
            .card { margin-bottom: 20px; }
        </style>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    """
    
    body = f"<h2>CPU Usage Report ({datetime.now().strftime('%Y-%m-%d')})</h2>"
    body += f"<p>Data source: {log_file}</p>"
    body += f"<p>Number of samples: {df['%User'].count()}</p>"
    
    body += generate_collapse_div(
        "CPU Data Table",
        df.to_html(index=False, classes="table table-bordered", justify="center")
    )
    
    body += generate_collapse_div(
        "%User",
        generate_collapse_div(
            "Usage Over Time",
            generate_line_chart(df["Time"].tolist(), df["%User"].tolist(), "%User")
        ) 
        + 
        generate_collapse_div(
            "Descriptive Statistics",
            generate_table(
                ["Metric", "Value"],
                [
                    ["Count", df["%User"].count()],
                    ["Median", df["%User"].median()],
                    ["Mean", df["%User"].mean()],
                    ["Max", df["%User"].max()],
                    ["Min", df["%User"].min()],
                    ["Sum", df["%User"].sum()],
                ]
            )
        )
    )
    
    body += generate_collapse_div(
        "%Nice",
        generate_collapse_div(
            "Usage Over Time",
            generate_line_chart(df["Time"].tolist(), df["%Nice"].tolist(), "%Nice")
        )
        +
        generate_collapse_div(
            "Descriptive Statistics",
            generate_table(
                ["Metric", "Value"],
                [
                    ["Count", df["%Nice"].count()],
                    ["Median", df["%Nice"].median()],
                    ["Mean", df["%Nice"].mean()],
                    ["Max", df["%Nice"].max()],
                    ["Min", df["%Nice"].min()],
                    ["Sum", df["%Nice"].sum()],
                ]
            )
        )
    )
    
    body += generate_collapse_div(
        "%System",
        generate_collapse_div(
            "Usage Over Time",
            generate_line_chart(df["Time"].tolist(), df["%System"].tolist(), "%System")
        )
        +
        generate_collapse_div(
            "Descriptive Statistics",
            generate_table(
                ["Metric", "Value"],
                [
                    ["Count", df["%System"].count()],
                    ["Median", df["%System"].median()],
                    ["Mean", df["%System"].mean()],
                    ["Max", df["%System"].max()],
                    ["Min", df["%System"].min()],
                    ["Sum", df["%System"].sum()],
                ]
            )
        )
    )
    
    body += generate_collapse_div(
        "%IOWait",
        generate_collapse_div(
            "Usage Over Time",
            generate_line_chart(df["Time"].tolist(), df["%IOWait"].tolist(), "%IOWait")
        )
        +
        generate_collapse_div(
            "Descriptive Statistics",
            generate_table(
                ["Metric", "Value"],
                [
                    ["Count", df["%IOWait"].count()],
                    ["Median", df["%IOWait"].median()],
                    ["Mean", df["%IOWait"].mean()],
                    ["Max", df["%IOWait"].max()],
                    ["Min", df["%IOWait"].min()],
                    ["Sum", df["%IOWait"].sum()],
                ]
            )
        )
    )
    
    body += generate_collapse_div(
        "%Steal",
        generate_collapse_div(
            "Usage Over Time",
            generate_line_chart(df["Time"].tolist(), df["%Steal"].tolist(), "%Steal")
        )
        +
        generate_collapse_div(
            "Descriptive Statistics",
            generate_table(
                ["Metric", "Value"],
                [
                    ["Count", df["%Steal"].count()],
                    ["Median", df["%Steal"].median()],
                    ["Mean", df["%Steal"].mean()],
                    ["Max", df["%Steal"].max()],
                    ["Min", df["%Steal"].min()],
                    ["Sum", df["%Steal"].sum()],
                ]
            )
        )
    )
    
    body += generate_collapse_div(
        "%Idle",
        generate_collapse_div(
            "Usage Over Time",
            generate_line_chart(df["Time"].tolist(), df["%Idle"].tolist(), "%Idle")
        )
        +
        generate_collapse_div(
            "Descriptive Statistics",
            generate_table(
                ["Metric", "Value"],
                [
                    ["Count", df["%Idle"].count()],
                    ["Median", df["%Idle"].median()],
                    ["Mean", df["%Idle"].mean()],
                    ["Max", df["%Idle"].max()],
                    ["Min", df["%Idle"].min()],
                    ["Sum", df["%Idle"].sum()],
                ]
            )
        )
    )
    
    body += "<p>Generated with <a href='https://github.com/niiicolai/sar-cpu-data-analyzer'>niiicolai/sar-cpu-data-analyzer</a></p>"
    
    with open(output, "w") as file:
        file.write(f"<!DOCTYPE html><html><head>{style}</head><body>")
        file.write(body)
        file.write("</body></html>")
