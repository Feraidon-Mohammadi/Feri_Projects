import hashlib

def generate_sha256(input_string):
    # Encode the input string to bytes
    input_bytes = input_string.encode('utf-8')

    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the input bytes
    sha256_hash.update(input_bytes)

    # Get the hexadecimal representation of the hash
    hashed_string = sha256_hash.hexdigest()

    return hashed_string

# Example: Hashing the string "Hello, World!"
result = generate_sha256("password")
print(result)