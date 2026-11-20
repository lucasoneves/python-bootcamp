student_scores = [20, 3000, 19, 9999999, 49, 12222, 39, 19, 4]

#print(max(student_scores))

choice = 0

for num in student_scores:
    if choice < num:
        choice = num
    
    
print(choice)