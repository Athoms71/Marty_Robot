import os


def read_file(file_path: str):
    """Read the contents of a file and returns a dictionnary containing pairs 'color' : '[left,right]'."""
    # Check if the file exists
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return {}
    couleurs = {}
    for line in lines:
        line = line.split(";")
        couleurs[line[0]] = [int(line[1]), int(line[2])]
    return couleurs


def write_file(file_path: str, content: str):
    """Write a string to a file with format 'color;left;right'."""
    # Check if the file exists
    try:
        with open(file_path, 'a') as file:
            file.write(content)
    except FileNotFoundError:
        print(f"File {file_path} not found. Creating a new file.")
