def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_number = how_many_words(text)
    letters = num_letters(text)
    print(f"The book contains {words_number} words.")
    print("\nLetter counts:")
    for char, count in letters.items():
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()


def how_many_words(text):
    words = text.split()
    return len(words)

def num_letters(text):
    num_dict = {}
    nums = text.lower()
    for char in nums:
        num_dict[char] = num_dict.get(char, 0) + 1
    return num_dict 

def sort_on(dict):
    return dict["num"]

main()