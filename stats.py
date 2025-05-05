# import collections

with open("./books/frankenstein.txt") as f:
    bookstring = f.read()


def get_num_words(book_as_string):
    num_words = len(book_as_string.split())
    print(f"Found {num_words} total words")


def get_char_count(book_as_string):
    book_as_string = book_as_string.lower()
    characters = {}
    for char in book_as_string:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def book_report(book_as_dict):
    book_as_dict = get_char_count(book_as_dict)
    book_as_dict = dict(
        sorted(book_as_dict.items(), key=lambda item: item[1], reverse=True)
    )
    for char in book_as_dict:
        if str(char).isalpha():
            print(f"{char}: {book_as_dict[char]}")


# def get_char_count(book_as_string):
#     counter = collections.Counter(book_as_string.lower())
#     print(dict(counter))
