import pandas

#TODO 1. Create a dictionary in this format:
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# my_dict = {}
# for (index, row) in alphabet.iterrows():
#     my_dict[row.letter] = row.code

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# user_input = input("Enter your word here: ").upper()
# code_words = ""
# for letter in user_input:
#     code_words += my_dict[letter]
#     code_words += " "
#
# print(code_words)


# Using Dictionary comprehension and list comprehension
phonetic_dict = {row.letter : row.code for (index, row) in alphabet.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word = input("Enter your word here: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()

