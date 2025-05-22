from stats import *
import sys

def main():
    # requires arg before executing code
    if len(sys.argv) == 2:
        book = sys.argv[1]

        # start of report
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        display_words_to_screen(book)
        print("--------- Character Count -------")
        sorted_chars = sort_them(book)
        for char_d in sorted_chars:

            char = char_d["char"]
            count = char_d["num"]

            print(f"{char}: {count}")
        print("============= END ===============")
        # end of report

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()