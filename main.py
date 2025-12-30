from stats import get_book_text, get_word_count, get_character_counts

frankenstein = "./books/frankenstein.txt"

def main():
    frankText = get_book_text("./books/frankenstein.txt")
    # print(frankText)
    get_word_count(frankText)
    frankChars = get_character_counts(frankText)
    print(frankChars)

main()
