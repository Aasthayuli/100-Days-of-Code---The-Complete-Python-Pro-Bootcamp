# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # print(key)
    # print(value)

import pandas

# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # print(row.student)
    # print(index)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

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

# Dictionary comprehension and list comprehension
phonetic_dict = {row.letter : row.code for (index, row) in alphabet.iterrows()}
print(phonetic_dict)
word = input("Enter your word here: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)