import pytest
from src.report.generate_table import generate_table

expected_html = """
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope='col'>test1</th><th scope='col'>test2</th>
                </tr>
            </thead>
            <tbody>
                <tr><th scope='row'>1</th><td>1</td><td>2</td></tr><tr><th scope='row'>2</th><td>3</td><td>4</td></tr>
            </tbody>
        </table>
    """

@pytest.mark.parametrize("options, expected", [
    ({"labels": ["test1", "test2"], "data": [[1, 2], [3, 4]]}, expected_html)
])
def test_generate_table_with_valid_partitions(options, expected):
    assert generate_table(options["labels"], options["data"]) == expected

@pytest.mark.parametrize("options, expected", [
    ({"labels": None, "data": [[1, 2], [3, 4]]}, "generate_table: Labels cannot be None"),
    ({"labels": ["test1", "test2"], "data": None}, "generate_table: Data cannot be None"),
    ({"labels": 1, "data": [[1, 2], [3, 4]]}, "generate_table: Labels must be a list"),
    ({"labels": ["test1", "test2"], "data": 1}, "generate_table: Data must be a list"),
    ({"labels": [], "data": [[1, 2], [3, 4]]}, "generate_table: Labels must have at least one element"),
    ({"labels": ["test1", "test2"], "data": []}, "generate_table: Data must have at least one element")
])
def test_generate_table_with_invalid_partitions(options, expected):
    with pytest.raises(ValueError, match=expected):
        generate_table(options["labels"], options["data"])
