from read_or_write_files import write_text_to_file


def decrypt_2(file_path: str, encrypted_text: str, decryption_dict: dict) -> None:
    """
    Decrypts the given encrypted text using the provided decryption dictionary.

    Args:
        file_path (str): The file path to write the decrypted text.
        encrypted_text (str): The text to be decrypted.
        decryption_dict (dict): A dictionary containing the mapping for decryption.

    Returns:
        None
    """
    decrypted_text = ''

    for char in encrypted_text:
        if char in decryption_dict:
            decrypted_text += decryption_dict[char]
        else:
            decrypted_text += char

    write_text_to_file(file_path, decrypted_text)
