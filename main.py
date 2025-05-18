from stats import display_words_to_screen, sort_them, book  

def main():
    # start of report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    display_words_to_screen()
    print("--------- Character Count -------")
    sorted_chars = sort_them()
    for char_d in sorted_chars:

        char = char_d["char"]
        count = char_d["num"]

        print(f"{char}: {count}")
    print("============= END ===============")

main()