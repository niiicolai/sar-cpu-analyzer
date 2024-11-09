from datetime import datetime

id = 0

def generate_collapse_div(title, html):
    global id
    id = id + 1
    
    return f"""
        <div class="card">
            <div class="card-header" id="heading-{id}">
                <h2 class="mb-0">
                    <button class="btn btn-link" type="button">
                        {title}
                    </button>
                </h2>
            </div>
            <div id="collapse-{id}" class="collapse">
                <div class="card-body">
                    {html}
                </div>
            </div>
        </div>
        <script>
                document.querySelector('#heading-{id} button').addEventListener('click', () => {{
                    const collapse = document.querySelector('#collapse-{id}');
                    if (collapse.classList.contains('show')) collapse.classList.remove('show');
                    else collapse.classList.add('show');
                }});
        </script>
    """

def generate_line_chart(labels, data, title):
    global id
    id = id + 1
    chart = """
        <canvas id="cpuChart%s"></canvas>
        <script>
        const ctx%s = document.getElementById('cpuChart%s').getContext('2d');
        const cpuChart%s = new Chart(ctx%s, {
            type: 'line',
            data: {
                labels: %s,
                datasets: [{
                    label: '%s',
                    data: %s,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            }
        });
        </script>
    """
    
    return chart % (id, id, id, id, id, labels, title, data)

def generate_table(labels, data, title):
    global id
    id = id + 1
    table = """
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    %s
                </tr>
            </thead>
            <tbody>
                %s
            </tbody>
        </table>
    """
    
    header = ""
    for label in labels:
        header += f"<th scope='col'>{label}</th>"
    
    body = ""
    for i, row in enumerate(data):
        body += "<tr>"
        body += f"<th scope='row'>{i + 1}</th>"
        for cell in row:
            body += f"<td>{cell}</td>"
        body += "</tr>"
    
    return table % (header, body)

def generate_html_report(df, output, log_file):
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
        "CPU User Over Time",
        generate_line_chart(df["Time"].tolist(), df["%User"].tolist(), "%User")
    )
    
    body += generate_collapse_div(
        "CPU System Over Time",
        generate_line_chart(df["Time"].tolist(), df["%System"].tolist(), "%System")
    )
    
    body += generate_collapse_div(
        "CPU IOWait Over Time",
        generate_line_chart(df["Time"].tolist(), df["%IOWait"].tolist(), "%IOWait")
    )
    
    body += generate_collapse_div(
        "CPU Steal Over Time",
        generate_line_chart(df["Time"].tolist(), df["%Steal"].tolist(), "%Steal")
    )
    
    body += generate_collapse_div(
        "CPU Idle Over Time",
        generate_line_chart(df["Time"].tolist(), df["%Idle"].tolist(), "%Idle")
    )
    
    body += generate_collapse_div(
        "CPU Nice Over Time",
        generate_line_chart(df["Time"].tolist(), df["%Nice"].tolist(), "%Nice")
    )
    
    body += generate_collapse_div(
        "CPU User Descriptive Statistics",
        generate_table(
            ["Metric", "Value"],
            [
                ["Count", df["%User"].count()],
                ["Median", df["%User"].median()],
                ["Mean", df["%User"].mean()],
                ["Max", df["%User"].max()],
                ["Min", df["%User"].min()],
                ["Total", df["%User"].sum()],
            ],
            "CPU User Descriptive Statistics"
        )
    )
    
    body += generate_collapse_div(
        "CPU System Descriptive Statistics",
        generate_table(
            ["Metric", "Value"],
            [
                ["Count", df["%System"].count()],
                ["Median", df["%System"].median()],
                ["Mean", df["%System"].mean()],
                ["Max", df["%System"].max()],
                ["Min", df["%System"].min()],
                ["Total", df["%System"].sum()],
            ],
            "CPU System Descriptive Statistics"
        )
    )
    
    body += generate_collapse_div(
        "CPU IOWait Descriptive Statistics",
        generate_table(
            ["Metric", "Value"],
            [
                ["Count", df["%IOWait"].count()],
                ["Median", df["%IOWait"].median()],
                ["Mean", df["%IOWait"].mean()],
                ["Max", df["%IOWait"].max()],
                ["Min", df["%IOWait"].min()],
                ["Total", df["%IOWait"].sum()],
            ],
            "CPU IOWait Descriptive Statistics"
        )
    )
    
    body += generate_collapse_div(
        "CPU Steal Descriptive Statistics",
        generate_table(
            ["Metric", "Value"],
            [
                ["Count", df["%Steal"].count()],
                ["Median", df["%Steal"].median()],
                ["Mean", df["%Steal"].mean()],
                ["Max", df["%Steal"].max()],
                ["Min", df["%Steal"].min()],
                ["Total", df["%Steal"].sum()],
            ],
            "CPU Steal Descriptive Statistics"
        )
    )
    
    body += generate_collapse_div(
        "CPU Idle Descriptive Statistics",
        generate_table(
            ["Metric", "Value"],
            [
                ["Count", df["%Idle"].count()],
                ["Median", df["%Idle"].median()],
                ["Mean", df["%Idle"].mean()],
                ["Max", df["%Idle"].max()],
                ["Min", df["%Idle"].min()],
                ["Total", df["%Idle"].sum()],
            ],
            "CPU Idle Descriptive Statistics"
        )
    )
    
    body += generate_collapse_div(
        "CPU Nice Descriptive Statistics",
        generate_table(
            ["Metric", "Value"],
            [
                ["Count", df["%Nice"].count()],
                ["Median", df["%Nice"].median()],
                ["Mean", df["%Nice"].mean()],
                ["Max", df["%Nice"].max()],
                ["Min", df["%Nice"].min()],
                ["Total", df["%Nice"].sum()],
            ],
            "CPU Nice Descriptive Statistics"
        )
    )
    
    body += "<p>Generated with <a href='https://github.com/niiicolai/sar-cpu-analyzer'>niiicolai/sar-cpu-analyzer</a></p>"
    
    with open(output, "w") as file:
        file.write(f"<!DOCTYPE html><html><head>{style}</head><body>")
        file.write(body)
        file.write("</body></html>")
