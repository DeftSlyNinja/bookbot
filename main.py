import sys
from stats import get_book_text, get_word_count, get_character_counts, report_stats

def main():
    if len(sys.argv) == 2:
        book = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookText = get_book_text(book)
    bookChars = get_character_counts(bookText)
    sorted_chars = report_stats(bookChars)
    # Print the program title
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    # Print Word Count Header
    print("----------- Word Count ----------")
    # Print Word Count
    print(f"Found {get_word_count(bookText)} total words")
    # Print Character Count Header
    print("--------- Character Count -------")
    # Print Print list of characters & their counts
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    # Print END
    print("============= END ===============")

main()
