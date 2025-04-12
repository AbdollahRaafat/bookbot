from stats import get_num_words
from stats import get_num_chars
from stats import sorted_dic
import sys

def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()


def main():
  if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  text = get_book_text(sys.argv[1])
  tuples = sorted_dic(get_num_chars(text))


  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {get_num_words(text)} total words")
  print("--------- Character Count -------")

  for item in tuples:
    print(f"{item[0]}: {item[1]}")

  print("============= END ===============")

main()


