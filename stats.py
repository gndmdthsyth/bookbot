def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def char_count(text):
    count = {}
    
    for c in text:
        lowered = c.lower()
        if lowered in count:
            count[lowered] +=1
        else:
            count[lowered] = 1
    return count

def sort_on(char_count):
    return char_count["num"]

def char_sort(count):
    sorted = []
    sorted_dict = {}
    for c in count:
        num = count[c]
        if c.isalpha():
            sorted.append({"char": c, "num" : num})
            #print(sorted)
    sorted.sort(reverse = True, key=sort_on)
    
    for char in sorted:
        #print(char)
        num = char["num"]
        c = char["char"]
        sorted_dict[c] = num

    return sorted_dict