def get_num_words(text):
    return len(text.split())

def character_count(text):
    text = text.lower()
    result = {}

    for char in text:
        char = char.lower()
        char_count = text.count(char)

        result[char] = char_count

    return result

def sort_on(items):
    return items["num"]

def format_char_count(counts):
    dicts = []

    for char, char_count in counts.items():
        char_dict = {}
        char_dict["char"] = char
        char_dict["num"] = char_count

        dicts.append(char_dict)
    
    dicts.sort(reverse=True, key=sort_on)

    return dicts
