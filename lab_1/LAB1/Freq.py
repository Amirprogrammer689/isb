from collections import Counter
from read_or_write_files import write_json_to_file


def analyze_character_frequency(text: str, file_path: str) -> None:
    """
    Analyze the frequency of characters in the given text and write the normalized frequency to a JSON file.

    Args:
        text (str): The input text to analyze.
        file_path (str): The file path to write the normalized frequency data.

    Returns:
        None
    """

    char_count = Counter(text)
    total_chars = sum(char_count.values())
    normalized_freq = {char: count / total_chars for char, count in char_count.items()}
    write_json_to_file(file_path, normalized_freq)

    return None


def create_decryption_key(file_path: str, char_freq_dict: dict, russian_alphabet_freq: dict) -> None:
    """
    Create a decryption key based on character frequency dictionaries and write it to a JSON file.

    Args:
        file_path (str): The file path to write the decryption key data.
        char_freq_dict (dict): Dictionary containing character frequencies.
        russian_alphabet_freq (dict): Dictionary containing frequencies of characters in the Russian alphabet.

    Returns:
        None
    """
    decryption_key = {}
    used_chars = set()

    for char in sorted(char_freq_dict, key=char_freq_dict.get, reverse=True):
        closest_match = max(russian_alphabet_freq,
                            key=lambda x: russian_alphabet_freq[x] if x not in used_chars else -1)
        decryption_key[char] = closest_match
        used_chars.add(closest_match)

    write_json_to_file(file_path, decryption_key)
