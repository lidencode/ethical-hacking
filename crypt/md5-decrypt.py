import hashlib
import sys

# Convert a text string in MD5 hash
def md5_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

# Parse the dictionary with the hash
def check_md5_in_file(file_path, md5_to_check):
    try:
        print(f"Searching '{md5_to_check}' in dictionary.")
        with open(file_path, 'r') as file:
            for line in file:
                clean_line = line.strip()
                md5_value = md5_hash(clean_line)

                if md5_value == md5_to_check:
                    print(f"HASH found: {clean_line}\r\n")
                    return

        print("HASH not found.\r\n")
    except FileNotFoundError:
        print(f"The file {file_path} don't exist.\r\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Use: python3 md5-decryot.py <folder/dictionary.txt> <hash_md5>")
        sys.exit(1)

    dictionary_file_path = sys.argv[1]
    hash_md5_to_check = sys.argv[2]

    # Check the MD5 Hash with the provided dictionary
    check_md5_in_file(dictionary_file_path, hash_md5_to_check)
