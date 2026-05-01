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
    return num_of_chars

def report(file_path):
    dict = number_of_characters(file_path)
    final = []
    for key in dict:
        final.append({"char": key, "num": dict[key]})
    
    num_of_words = get_book_text(file_path)

    print(f""""
          ============ BOOKBOT ============
        Analyzing book found at books/frankenstein.txt...
                ----------- Word Count ----------
                        Found {num_of_words} total words
                --------- Character Count -------
          """)