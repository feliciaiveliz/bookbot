import sys
from stats import get_num_words, character_count, format_char_count

def get_book_text(file_path):
    file_contents = ""

    with open(file_path) as file:
        file_contents = file.read()

    return file_contents

def main():
    cl_args = sys.argv

    if len(cl_args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = cl_args[1]
    contents = get_book_text(f"./{file_path}")
    word_count = get_num_words(contents)
    char_count = character_count(contents)
    sorted_char_nums = format_char_count(char_count)
    chars = {}
    
    for sorted_char in sorted_char_nums:
        char = sorted_char["char"]
        number = sorted_char["num"]

        if not char.isalpha():
            continue

        chars[char] = number

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter, number in chars.items():
        print(f"{letter}: {number}")
    print("============= END ===============")

main()