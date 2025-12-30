def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(text):
    words = text.split()
    wc = len(words)
    print(f"Found {wc} total words")

def get_character_counts(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items['num']

def report_stats(dict):
    dict_list = []
    for char, num in dict.items():
        if char.isalpha():
            new_dict = {'char': char, 'num': num}
            dict_list.append(new_dict)
        else:
            continue
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list