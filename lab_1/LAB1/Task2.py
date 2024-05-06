from Decryption_task_2 import decrypt_2
from Freq import analyze_character_frequency, create_decryption_key
from read_or_write_files import read_text_from_file, read_json_from_file

if __name__ == "__main__":
    config_data = read_json_from_file("Paths.json")
    text = read_text_from_file(config_data["text_2_file_path"])

    analyze_character_frequency(text, config_data["freq_2_path"])
    freq = read_json_from_file(config_data["freq_2_path"])
    data = read_json_from_file(config_data["data_2_path"])
    create_decryption_key(config_data["decryption_key_file_2_path"], freq, data)

    key = read_json_from_file(config_data["decryption_key_file_2_path"])
    decrypt_2(config_data["decrypted_text_2_file_path"], text, key)
