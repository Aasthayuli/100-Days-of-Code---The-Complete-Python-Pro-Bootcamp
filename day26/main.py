#
# import random
#
# numbers = [1,2,3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)
#
#
# name = "Aasthayuli"
# letters_list = [letter for letter in name]
# print(letters_list)
#
#
# new_range = [n*2 for n in range(1,5)]
# print(new_range)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name)<5]
# print(short_names)
#
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)
#
#
# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)
# passed_students = {student:student_scores[student] for student in student_scores if student_scores[student] >= 60}
# print(passed_students)
# # OR
# passed = {student:score for (student,score) in student_scores.items() if score >= 60}
# print(passed)

# Looping through dictionaries
student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}
# for (key, value) in student_dict.items():
#     print(key)
# for (key, value) in student_dict.items():
#     print(value)


import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame
# for (key,value) in student_data_frame.items():
#     print(key)

# for (key,value) in student_data_frame.items():
#     print(value)

# Loop through rows of a dataframe
# for (index, row) in student_data_frame.iterrows():
    # print(index)

# for (index, row) in student_data_frame.iterrows():
    # print(row)

# for (index, row) in student_data_frame.iterrows():
    # print(row.student)

# for (index, row) in student_data_frame.iterrows():
    # print(row.score)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
