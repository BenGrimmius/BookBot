def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
        split_content = content.split()
        num_words = len(split_content)
        print(f"Found {num_words} total words")
        return num_words

def number_of_characters(file_path):
    num_of_chars = {}
    count = 1

    with open(file_path) as f:
        content = f.read().split()
        for word in content:
            for char in word:
                char_lower = char.lower()
                if char_lower not in num_of_chars:
                    num_of_chars[char_lower] = 1
                else:
                    num_of_chars[char_lower] += 1
    print(num_of_chars)
    return num_of_chars

def report(file_path):
    dict = number_of_characters(file_path)
    pass    