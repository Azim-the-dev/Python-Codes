# Write a Program to calculate total marks, percentage and grade of a student. Marks  obtained in each of the three subjects are to be input by the user. Assign grades according  to the following criteria:  
# Grade A: Percentage >= 80  
# Grade B: Percentage >= 70 and < 80  
# Grade C: Percentage >= 60 and < 70  
# Grade D: Percentage >= 40 and < 60  
# Grade E: Percentage < 40 

subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

total_marks = subject1 + subject2 + subject3

percentage = (total_marks / 300) * 100

if(percentage >= 80):
    grade = 'A'
elif(percentage >= 70 and percentage < 80):
    grade = 'B'
elif(percentage >= 60 and percentage < 70):
    grade = 'C'
elif(percentage >= 40 and percentage < 60):
    grade = 'D'
else:
    grade = 'E'

print("You have total ", total_marks, " marks")
print("You have ", percentage, "% percentage")
print("You are '", grade, "' grade")