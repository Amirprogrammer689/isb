from read_or_write_files import read_text_from_file, write_text_to_file, read_json_from_file
from Encryption_and_decryption import caesar_cipher_encrypt, caesar_cipher_decrypt

if __name__ == "__main__":
    config_data = read_json_from_file("Paths.json")
    text = read_text_from_file(config_data["text_file_path"])
    key_data = read_json_from_file(config_data["key_file_path"])
    key = key_data["caesar_cipher_key"]

    encrypted_text = caesar_cipher_encrypt(text, key)
    decrypted_text = caesar_cipher_decrypt(encrypted_text, key)

    write_text_to_file(config_data["encrypted_file_path"], encrypted_text)
    write_text_to_file(config_data["decrypted_file_path"], decrypted_text)
