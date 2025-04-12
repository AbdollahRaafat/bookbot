def get_num_words(book_text):
  text_words = book_text.split()
  return len(text_words)

def get_num_chars(book_text):
  book_text = book_text.lower()
  chr_counter = {}

  for char in book_text:
      if not char.isalpha():
        continue
      if char in chr_counter :
          chr_counter[char] += 1
      else:
          chr_counter[char] = 1

  return chr_counter

def sorted_dic(dict):
  pair_listing = list(dict.items())
  pair_listing.sort(key=lambda a: a[1], reverse=True)
  return pair_listing

