from NIST_tests import *


if __name__ == "__main__":
    config = read_json_from_file("path.json")
    sequences = read_json_from_file(config["from"])
    sequences_cpp = sequences["C++"]
    sequences_java = sequences["Java"]
    nist_frequency_bit_test(sequences_cpp, config["to"], "C++")
    nist_frequency_bit_test(sequences_java, config["to"], "Java")
    nist_identical_serial_bits(sequences_cpp, config["to"], "C++")
    nist_identical_serial_bits(sequences_java, config["to"], "Java")
    nist_longest_sequence(sequences_cpp, config["to"], "C++")
    nist_longest_sequence(sequences_java, config["to"], "Java")
