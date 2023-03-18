def print_upper_words(words):
    """For a list of words, print out each word on a separate line, but all uppercase"""
    for word in words:
        print(word.upper())



def print_upper_words_2(words):
    """print each word that starts with e or E on a separate line"""
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """print each word that starts with the letters entered"""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break