import json


def write_text_to_file(file_path: str, text: str) -> None:
    """
    Write text data to a file.
    Parameters:
    file_path (str): The path to the file to write.
    text (str): The text to write to the file.
    """
    try:
        with open(file_path, 'a+', encoding='utf-8') as file:
            file.write(text)
        print("The information is successfully saved to the file.")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def read_json_from_file(file_path: str) -> dict:
    """
    Read JSON data from a file.
    Parameters:
    file_path (str): The path to the JSON file to read.
    Returns:
    dict: The JSON data read from the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except json.JSONDecodeError as e:
        print(f"Error while decoding JSON: {e}")
    except Exception as e:
        print(f"An error has occurred: {e}")


def read_binary_from_file(file_path: str) -> bytes:
    """
    Read binary data from a file.
    Parameters:
    file_path (str): The path to the file to read.
    Returns:
    bytes: The binary data read from the file.
    """
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        return data
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


def write_binary_to_file(file_path: str, bytes_text: bytes) -> None:
    """
    Write binary data to a file.
    Parameters:
    file_path (str): The path to the file to write.
    bytes_text (bytes): The binary data to write to the file.
    """
    try:
        with open(file_path, 'wb') as file:
            file.write(bytes_text)
        print("The binary data has been successfully saved to the file.")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred while writing the binary data to the file: {e}")
