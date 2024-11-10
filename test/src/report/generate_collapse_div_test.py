import pytest
from src.report.generate_collapse_div import generate_collapse_div

expected_html = """
        <div class="card">
            <div class="card-header" id="heading-1">
                <h2 class="mb-0">
                    <button class="btn btn-link" type="button">
                        test
                    </button>
                </h2>
            </div>
            <div id="collapse-1" class="collapse">
                <div class="card-body">
                    test
                </div>
            </div>
        </div>
        <script>
                document.querySelector('#heading-1 button').addEventListener('click', () => {
                    const collapse = document.querySelector('#collapse-1');
                    if (collapse.classList.contains('show')) collapse.classList.remove('show');
                    else collapse.classList.add('show');
                });
        </script>
    """

@pytest.mark.parametrize("options, expected", [
    ({"title": "test", "html": "test"}, expected_html)
])
def test_generate_collapse_div_with_valid_partitions(options, expected):
    assert generate_collapse_div(options["title"], options["html"]) == expected
    
@pytest.mark.parametrize("options, expected", [
    ({"title": None, "html": "test"}, "generate_collapse_div: Title cannot be None"),
    ({"title": "test", "html": None}, "generate_collapse_div: HTML cannot be None"),
    ({"title": 1, "html": "test"}, "generate_collapse_div: Title must be a string"),
    ({"title": "test", "html": 1}, "generate_collapse_div: HTML must be a string")
])
def test_generate_collapse_div_with_invalid_partitions(options, expected):
    with pytest.raises(ValueError, match=expected):
        generate_collapse_div(options["title"], options["html"])
