from stats import get_num_words, get_chars_dict, get_sorted_chars
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    num_words = get_num_words(book_content) 
    chars_dict = get_chars_dict(book_content)
    sorted_chars = get_sorted_chars(chars_dict)

    print(f"Found {num_words} total words")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Total words: {num_words}")
    print("--------- Character Count -------")
    
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

    
main()
