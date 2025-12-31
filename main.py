from stats import get_book_text, get_word_count, get_character_counts, report_stats
frankenstein = "./books/frankenstein.txt"

def main():
    frankText = get_book_text("./books/frankenstein.txt")
    frankChars = get_character_counts(frankText)
    sorted_chars = report_stats(frankChars)
    # Print the program title
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {frankenstein}")
    # Print Word Count Header
    print("----------- Word Count ----------")
    # Print Word Count
    print(f"Found {get_word_count(frankText)} total words")
    # Print Character Count Header
    print("--------- Character Count -------")
    # Print Print list of characters & their counts
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    # Print END
    print("============= END ===============")

main()
