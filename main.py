import sys
from stats import get_num_words, get_chars_dict, get_sorted_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = get_sorted_chars(chars_dict)
    print_report(book_path, num_words, sorted_chars)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_chars:
        if not c["char"].isalpha():
            continue
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

main()