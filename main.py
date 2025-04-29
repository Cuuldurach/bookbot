import sys
from stats import get_num_words, get_num_chars, sort_num_chars

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text (book_filepath):
    with open (book_filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(sys.argv[1])
    word_count = get_num_words(book_text)
    letter_count = get_num_chars(book_text)
    sorted_letter_count = sort_num_chars(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_letter_count:
        char = char_dict["char"]
        if char.isalpha():
             print(f"{char}: {char_dict['num']}")
    print("============= END ===============")

main()