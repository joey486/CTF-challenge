from Crypto.Cipher import AES
import base64

# Key and IV should be the same as used in the encryption
key = b'thisisthekey1234'  # 16 bytes key for AES-128
iv = b'thisistheiv12345'   # 16 bytes IV for AES

def unpad(data):
    # PKCS5 Unpadding
    padding = data[-1]
    return data[:-padding]

def decrypt(encoded_text, key):
    decoded_data = base64.b64decode(encoded_text)
    iv = decoded_data[:16]  # Extract the IV from the beginning of the decoded data
    encrypted_text = decoded_data[16:]  # The rest is the encrypted message

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text))
    return decrypted_text.decode('utf-8')

# Encrypted content (Example, replace with actual encrypted text)
encoded_text = 'dGhpc2lzdGhlaXYxMjM0NSxTvyAwNuKYWoEUaS3VX7zIHlJkeY2Us22fkWSGPFG/zZNen0QbgPren2CMh/vaVxFw6QRODzOyEdRp1qWHUX0i681p2DA68YQo9I6ngkUSAqadT10xKcYV27TUYvWjwKgrEdRm0R5HLAcQ4mOh+2W2o8rkWDFlNWgwAosED4bTA1kHual+kWfcbGJg+O/feAOBBPYyqWHN/nDFMGiHcL1rxNQRpnIpBS5BEsV1DUeV5vi+3DTCHGcjpdkp0m7jy3eWMzEVQdT4qNv+6zreq+2XTWKe+WSDVqi94k/EXZuEOGw54NeBOa8GbKLb+mXZrjRRd8hS2NIIUd7EKLbOvi8tE2gnjKqkt3w6uRy+x26Yd7a2HPRGWCgnbGK3Zs6HCjQQa/AB3I4itKHgG2LS3qxFJOapjho37hU77hKbA1DZW2VfpPjiZVDZsoKnuyYLTSKj/K+AdwPhCXDxXxHfzCjTUJ1wzt45HpEoRomfDPhOWha/XlC5r/cOaoso7vyMha42q/+AiBsFXokUfMXqcXYIbuw+8NhLk2XsEEkgApqIbCNFrt5cCU9XVkLXdPpp1tJDR/+un1oX5OjD8evpKzr04yv6MYc1NPXd8YeYyAzQ+mIsQoJgqNeqRp8k4Zajr9jSeljE+2b+jl2o76w7Z9d/ZJ2d0o2h+Bfyd6vi/wEaEjZJFLl9DOKrYma4iCOi7UaMJNuhO41jNcqkrGuoLxpgTbEMl8Or/cgFFdZBmZO8J1PP6GM4qvp/2VXSp979KBf8H14k+Z2jVQddHGRetk9ykzrnsYIIaPFRBZMjdmrorTw7ik0dnaYvGcTmooItjKo+JhCQLfYKHR0cTcre5YMnZ/ZTzQEfjcg/2slHBDMigO4IC99lydQZX1LHJLx4nFra4K5hntJJPOEc4Ar5DC4rSWFfi726jSmKl9e5urP0hpBS4nqKWpaBntQ1gzOj9w=='

# Decrypt the content
decrypted_text = decrypt(encoded_text, key)
print(f"Decrypted text: {decrypted_text}")
