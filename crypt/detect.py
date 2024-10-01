import sys
import re
import base64
import codecs

def detect_crypt(text):
    result = []

    # Check Base64
    try:
        if len(text) % 4 == 0 and re.match(r'^[A-Za-z0-9+/]+={0,2}$', text):
            base64.b64decode(text)
            result.append("Base64")
    except Exception:
        pass

    # Check Hexadecimal
    if re.match(r'^[0-9a-fA-F]+$', text):
        result.append("Hexadecimal")

    # Check ROT13
    try:
        rot13 = codecs.decode(text, 'rot_13')
        if re.match(r'^[A-Za-z0-9 ]+$', rot13):
            result.append("ROT13")
    except Exception:
        pass

    # Check MD5, SHA-1 o SHA-256
    if len(text) == 32 and re.match(r'^[0-9a-fA-F]+$', text):
        result.append("MD5")
    elif len(text) == 40 and re.match(r'^[0-9a-fA-F]+$', text):
        result.append("SHA-1")
    elif len(text) == 64 and re.match(r'^[0-9a-fA-F]+$', text):
        result.append("SHA-256")

    if not result:
        return "Unknown HASH Crypt"
    
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python3 detect.py <string>")
        sys.exit(1)

    string = sys.argv[1]
    print(f"Try to detect HASH Crypt: '{string}'\r")
    print(detect_crypt(string))
