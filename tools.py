def read_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading from {file_path.split('/')[-1]}: {e}")
        return None


def write_to_file(file_path, content):
    try:
        with open(file_path, "w", encoding="utf-8", errors="replace") as file:
            file.write(content)
        print(f"Content successfully written to '{file_path}'.")
    except Exception as e:
        print(f"Error writing to {file_path.split('/')[-1]}: {e}")
