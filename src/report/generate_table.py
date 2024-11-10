
id = 0

def generate_table(labels, data):
    global id
    id = id + 1
    
    if labels is None:
        raise ValueError("generate_table: Labels cannot be None")
    if data is None:
        raise ValueError("generate_table: Data cannot be None")
    if not isinstance(labels, list):
        raise ValueError("generate_table: Labels must be a list")
    if not isinstance(data, list):
        raise ValueError("generate_table: Data must be a list")
    if len(labels) < 1:
        raise ValueError("generate_table: Labels must have at least one element")
    if len(data) < 1:
        raise ValueError("generate_table: Data must have at least one element")
    
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
