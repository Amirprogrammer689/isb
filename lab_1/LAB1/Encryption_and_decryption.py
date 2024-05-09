ALPHABET_RUS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890 :;,.!?{}()-+=_"'


def caesar_cipher_encrypt(text: str, key: int) -> str:
    """
    Encrypts the text using Caesar cipher.

    Parameters:
    text (str): The text to be encrypted.
    key (int): The encryption key.

    Returns:
    str: The encrypted text.
    """
    encrypted_text = ''
    alphabet = ALPHABET_RUS

    for char in text:
        if char in alphabet:
            index = alphabet.find(char)
            encrypted_index = (index + key) % len(alphabet)
            encrypted_text += alphabet[encrypted_index]
        else:
            encrypted_text += char

    return encrypted_text


def caesar_cipher_decrypt(text: str, key: int) -> str:
    """
    Decrypts the text using Caesar cipher.

    Parameters:
    text (str): The text to be decrypted.
    key (int): The decryption key.

    Returns:
    str: The decrypted text.
    """
    return caesar_cipher_encrypt(text, -key)
