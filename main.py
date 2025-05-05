import sys
from stats import get_num_words, get_num_letters, sort_report


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else :
        bookpath=sys.argv[1]
        print ("============ BOOKBOT ============")
        print (f"Analyzing book found at {bookpath}")
        num_words =get_num_words(bookpath)
        print ("----------- Word Count ----------")
        print (f"Found {num_words} total words")
        num_letters = get_num_letters(bookpath)
        #print (num_letters)
        sorted=sort_report(num_letters)
        print ("--------- Character Count -------")
        for i in sorted:

            if i["char"].isalpha():
                print (f"{i["char"]}: {i["num"]}")
        print ("============= END ===============")

   

main()