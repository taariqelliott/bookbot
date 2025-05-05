from stats import get_num_words, get_char_count, book_report
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    bookpath = sys.argv[1]
    book_bot_title = "============ BOOKBOT ============"
    book_bot_path = "books/frankenstein.txt..."
    word_count = "----------- Word Count ----------"
    char_count = "--------- Character Count -------"
    end_statement = "============= END ==============="

    try:
        with open(bookpath) as f:
            bookstring = f.read()
    except:
        print("no")

    print(book_bot_title)
    print(f"Analyzing book found at {book_bot_path}")
    print(word_count)
    get_num_words(bookstring)
    print(char_count)
    book_report(bookstring)
    print(end_statement)
    print(get_char_count(bookstring))


if __name__ == "__main__":
    main()
