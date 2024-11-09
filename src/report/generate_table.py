
id = 0

def generate_table(labels, data):
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
