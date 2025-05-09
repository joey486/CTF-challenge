from Crypto.Cipher import AES
import base64
import os

# Key and IV (Initialization Vector)
key = b'thisisthekey1234'  # 16 bytes key for AES-128
iv = b'thisistheiv12345'   # 16 bytes IV for AES

def pad(data):
    # PKCS5 Padding
    padding = 16 - len(data) % 16
    return data + (chr(padding) * padding).encode()

def encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_text = cipher.encrypt(pad(plaintext.encode()))
    return base64.b64encode(iv + encrypted_text).decode('utf-8')

# Plaintext content
plaintext = """
Here’s the updated text file with additional random text:

```
Sample Data File
----------------
Name: John Doe
Email: john.doe@example.com
Phone: +1-234-567-890
Address: 1234 Elm Street, Anytown, USA

Occupation: Software Engineer
Company: Tech Innovators Inc.
Date of Birth: January 1, 1985

Additional Notes:
- http://yossiheifetzproject1.atwebpages.com/.
- You can add more information as needed.
- Preferred Contact Method: Email
- Known Languages: English, Spanish
- Hobbies: Hiking, Reading, Coding
- Last Login: August 16, 2024
- Account Status: Active
```

This version includes more details such as occupation, company, date of birth, and hobbies. Let me know if you need any specific information added!
"""

# Encrypt the content
encrypted_text = encrypt(plaintext, key, iv)
output_file = "encrypted_output.txt"
with open(output_file, "w") as file:
    file.write(encrypted_text)

print(f"Encrypted text has been saved to '{output_file}'.")
