from stats import count_words
from stats import get_frequency
from stats import sorted_dict_to_list
import sys

def get_book_text(path_to_file):
  file_contents = ""
  with open(path_to_file) as f:
    file_contents = f.read()
  return file_contents

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  path = sys.argv[1]
  contents = get_book_text(path)
  num_words = count_words(contents)
  frequency = get_frequency(contents)
  # print(f"{num_words} words found in the document")
  # print(f"{frequency}")

  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for item in sorted_dict_to_list(frequency):
    if item["char"].isalpha():
      key =item["char"]
      v = item["num"]
      print(f"{key}: {v}")

  print("============= END ===============")

if __name__=="__main__":
  main()