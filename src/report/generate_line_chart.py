
id = 0

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
