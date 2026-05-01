def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
        split_content = content.split()
        num_words = len(split_content)
        print(f"Found {num_words} total words")
        return num_words

def number_of_characters(file_path):
    pass