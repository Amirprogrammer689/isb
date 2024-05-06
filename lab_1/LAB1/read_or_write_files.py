import json


def read_text_from_file(file_path: str) -> str:
    """
    Read text data from a file.

    Parameters:
    file_path (str): The path to the file to read.

    Returns:
    str: The text read from the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error has occurred: {e}")


def write_text_to_file(file_path: str, text: str) -> None:
    """
    Write text data to a file.

    Parameters:
    file_path (str): The path to the file to write.
    text (str): The text to write to the file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print("The information is successfully saved to the file.")
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
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError as e:
        print(f"Error while decoding JSON: {e}")
    except Exception as e:
        print(f"An error has occurred: {e}")


def write_json_to_file(file_path: str, data: dict, indent: int = 4) -> None:
    """
    Write JSON data to a file.

    Parameters:
    file_path (str): The path to the file to write.
    data (dict): The JSON data to write to the file.
    indent (int): The number of spaces for indentation in the JSON output (default is 4).
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=indent)
        print("Data was successfully written to a file in JSON.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
