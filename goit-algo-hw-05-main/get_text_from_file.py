def get_text_from_file(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    return file_content
