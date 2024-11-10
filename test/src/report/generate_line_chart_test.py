import pytest
from src.report.generate_line_chart import generate_line_chart

expected_html = """
        <canvas id="cpuChart1"></canvas>
        <script>
        const ctx1 = document.getElementById('cpuChart1').getContext('2d');
        const cpuChart1 = new Chart(ctx1, {
            type: 'line',
            data: {
                labels: ['1', '2', '3'],
                datasets: [{
                    label: 'test',
                    data: [1, 2, 3],
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            }
        });
        </script>
    """
@pytest.mark.parametrize("options, expected", [
    ({
        "labels": ["1", "2", "3"],
        "data": [1, 2, 3],
        "title": "test"
     }, expected_html)
])
def test_generate_line_chart_with_valid_partitions(options, expected):
    assert generate_line_chart(options["labels"], options["data"], options["title"]) == expected
    
@pytest.mark.parametrize("options, expected", [
    ({"labels": None, "data": [1, 2, 3], "title": "test"}, "generate_line_chart: Labels cannot be None"),
    ({"labels": ["1", "2", "3"], "data": None, "title": "test"}, "generate_line_chart: Data cannot be None"),
    ({"labels": ["1", "2", "3"], "data": [1, 2, 3], "title": None}, "generate_line_chart: Title cannot be None"),
    ({"labels": 1, "data": [1, 2, 3], "title": "test"}, "generate_line_chart: Labels must be a list"),
    ({"labels": ["1", "2", "3"], "data": 1, "title": "test"}, "generate_line_chart: Data must be a list"),
    ({"labels": ["1", "2", "3"], "data": [1, 2, 3], "title": 1}, "generate_line_chart: Title must be a string"),
    ({"labels": [], "data": [1, 2, 3], "title": "test"}, "generate_line_chart: Labels must have at least one element"),
    ({"labels": ["1", "2", "3"], "data": [], "title": "test"}, "generate_line_chart: Data must have at least one element")
])
def test_generate_line_chart_with_invalid_partitions(options, expected):
    with pytest.raises(ValueError, match=expected):
        generate_line_chart(options["labels"], options["data"], options["title"])
