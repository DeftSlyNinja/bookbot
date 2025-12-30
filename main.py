from stats import get_book_text, get_word_count, get_character_counts, report_stats

frankenstein = "./books/frankenstein.txt"

def main():
    frankText = get_book_text("./books/frankenstein.txt")
    # print(frankText)
    # get_word_count(frankText)
    frankChars = get_character_counts(frankText)
    # print(frankChars)
    sorted_chars = report_stats(frankChars)
    for item in sorted_chars:
        print(item)

main()
