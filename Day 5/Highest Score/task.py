student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]


#_____________________________________________________________
total_exam_score = sum(student_scores)  # built-in function
print(total_exam_score)

Sum=0
for score in student_scores:
    Sum+=score

print(Sum)

#__________________________________________________________________________
print(max(student_scores))     # built-in function

Max=0
for score in student_scores:
    if score > Max:
        Max=score

print(Max)

#__________________________________________________________________________

