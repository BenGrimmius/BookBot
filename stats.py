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
    list_of_dict = []
    for key in dict:
        list_of_dict.append({"char": key, "num": dict[key]})
    
    num_of_words = get_book_text(file_path)

    def sort_on(item):
        return item["num"]
    
    list_of_dict.sort(reverse=True,  key=sort_on)

    printed_ls = def printed_list():
        for key in list_of_dict:
            print(f"{key}")


   
        # print("============ BOOKBOT ============")
        # ("Analyzing book found at {file_path}..")
        # ("----------- Word Count ----------")
        # (" Found {num_of_words} total words")
        # ("--------- Character Count -------")
