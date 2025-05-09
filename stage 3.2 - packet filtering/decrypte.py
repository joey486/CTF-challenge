with open("extracted.hex", "r") as file:
    hex_content = file.read()

text_content = bytes.fromhex(hex_content).decode("utf-8")

with open("extracted.txt", "w") as file:
    file.write(text_content)
