import sys
from stats import word_count, char_count, get_book_text, char_sort
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_title = sys.argv[1]
    text = get_book_text(book_title)
    words = word_count(text)
    sorted_chars = char_sort(char_count(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_title}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    #print(sorted_chars)
    for char in sorted_chars:
        print(f"{char}: {sorted_chars[char]}")
    print("============= END ===============")

main()