with open("favicon.ico", "ab") as favicon:
    with open("url.hex", "r") as hexfile:
        hex_data = hexfile.read()
        favicon.write(bytes.fromhex(hex_data))
