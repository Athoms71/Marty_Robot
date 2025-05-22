def read_file(file_path):
    """Read the contents of a file and returns a dictionnary containing pairs 'color:value'."""
    # Check if the file exists
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return {}
    couleurs = {}
    for line in lines:
        line = line.split(":")
        couleurs[line[0].strip()] = line[1].strip()
    return couleurs


def write_file(file_path, content: str):
    """Write a string to a file with format 'color:value'."""
    # Check if the file exists
    try:
        with open(file_path, 'r') as file:
            file.write(content)
    except FileNotFoundError:
        print(f"File {file_path} not found. Creating a new file.")
