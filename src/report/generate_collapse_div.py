
id = 0

def generate_collapse_div(title, html):
    global id
    id = id + 1
    
    if title is None:
        raise ValueError("generate_collapse_div: Title cannot be None")
    if html is None:
        raise ValueError("generate_collapse_div: HTML cannot be None")
    if not isinstance(title, str):
        raise ValueError("generate_collapse_div: Title must be a string")
    if not isinstance(html, str):
        raise ValueError("generate_collapse_div: HTML must be a string")    
    
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
    