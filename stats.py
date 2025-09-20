def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        print(file_contents)

def word_count(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
        print(f"{num_words} words found in the document")

def char_count(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        