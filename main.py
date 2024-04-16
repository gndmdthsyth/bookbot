def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    num_words = count_words(text)
    #print(f"{num_words} words in the document")
    print(count_letters(text))

def get_book_path(path):

    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return none

main()