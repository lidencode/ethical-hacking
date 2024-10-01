import hashlib
import sys

# Convert a text string in MD5 hash
def md5_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Use: python3 md5-cryot.py <string>")
        sys.exit(1)

    string_to_crypt = sys.argv[1]

    # Crypt the argument to MD5
    result = md5_hash(string_to_crypt)
    print(f"MD5 Hash: '{result}'\r")