
id = 0

def generate_line_chart(labels, data, title):
    global id
    id = id + 1
    
    if labels is None:
        raise ValueError("generate_line_chart: Labels cannot be None")
    if data is None:
        raise ValueError("generate_line_chart: Data cannot be None")
    if title is None:
        raise ValueError("generate_line_chart: Title cannot be None")
    if not isinstance(labels, list):
        raise ValueError("generate_line_chart: Labels must be a list")
    if not isinstance(data, list):
        raise ValueError("generate_line_chart: Data must be a list")
    if not isinstance(title, str):
        raise ValueError("generate_line_chart: Title must be a string")
    if len(labels) < 1:
        raise ValueError("generate_line_chart: Labels must have at least one element")
    if len(data) < 1:
        raise ValueError("generate_line_chart: Data must have at least one element")
    
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
