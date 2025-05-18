
def get_book_text(filepath):
    # opens the file
    with open(filepath) as f:
        # reads the file
        file_contents = f.read()
    # returns the file from the function
    return file_contents

def count_words(file_contents):
    # accepts the text from the book 
    # as a string inside of a list
    book_to_string = file_contents.split()

    # counts the number of words in the list
    total_words = len(book_to_string)

    # returns the number of words in the list
    return f"Found {total_words} total words"

def display_words_to_screen(book):
    # uses first function
    read_book = get_book_text(book)

    # uses second function
    word_count = (count_words(read_book))

    # prints to console
    print(word_count)

def num_times_each_char(book):
    my_dict = {}
    # takes text from book as string then
    # returns the number of times each char

    # display the book
    bts = get_book_text(book)
    #print(bts)

    # count every single character in book
    # and make lowercase
    for character in bts:
        #print(character.lower())

        key = character.lower()

        if key in my_dict:
            my_dict[key] += 1
        else:
            my_dict[key] = 1

    return my_dict

def sort_them(book):
    char_dict = num_times_each_char(book)
    chars_list = list()
    #print(chars_list)
    # print(char_dict)
    for char, count in char_dict.items():
        # print(char, count)
        if char.isalpha():
            chars_list.append({"char": char, "num": count})
        #print(char, count)
    #print(chars_list)

    def sort_on(dict):
        return dict["num"]

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list

