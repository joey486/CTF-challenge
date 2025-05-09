# hex_converter.py

def convert_text_to_hex(input_file_path, output_file_path):
    try:
        with open(input_file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        hex_content = content.encode("utf-8").hex()
        
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(hex_content)
        
        print(f"Hexadecimal content successfully written to {output_file_path}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Using forward slashes for paths
    input_path = "./url.txt"
    output_path = "./url.hex"
    
    convert_text_to_hex(input_path, output_path)
