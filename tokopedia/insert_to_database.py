import json

def read_json_file(file_path):
    """Reads a JSON file and returns its contents as a Python object.

    Args:
        file_path: The path to the JSON file.

    Returns:
        The parsed JSON data as a Python object.
    """

    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Example usage:
file_path = 'tokopedia/detail-products.json'
data = read_json_file(file_path)
print(data[0])
