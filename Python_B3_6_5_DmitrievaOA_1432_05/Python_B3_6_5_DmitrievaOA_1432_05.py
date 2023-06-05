# Python_B3_6_5_DmitrievaOA_1432_05

def create_word_set():
  words = input("Enter a list of words separated by commas: ").split(",") # Введите список слов, разделенных запятыми:
  word_set = set(words)
  return word_set

def count_words():
  words = input("Enter a list of words separated by commas: ").split(",") # Введите список слов, разделенных запятыми: 
  count = len(words)
  print("Number of words:", count) # Количество слов:

def create_dictionary():
  words = input("Enter a list of words separated by commas: ").split(",") # Введите список слов, разделенных запятыми: 
  second_list = input("Enter a list of words with the same number of characters: ").split(",") # Введите список слов с одинаковым количеством символов:
  dictionary = dict(zip(words, second_list))
  print(dictionary)

word_set = create_word_set()
count_words()
create_dictionary()
