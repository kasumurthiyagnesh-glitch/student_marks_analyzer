# Student Marks Analyzer 

students = {}

n = int(input("Enter number of students: "))

# Input data
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\n--- Student Records ---")

# Convert keys to list to access first element
names = list(students.keys())

# Initialize using first element
topper = names[0]
lowest_student = names[0]
highest_marks = students[topper]
lowest_marks = students[lowest_student]

total = 0
pass_count = 0

for name in students:
    marks = students[name]
    total += marks

    # Highest
    if marks > highest_marks:
        highest_marks = marks
        topper = name

    # Lowest
    if marks < lowest_marks:
        lowest_marks = marks
        lowest_student = name

    # Pass/Fail
    if marks > 50:
        pass_count += 1
        status = "Pass"
    else:
        status = "Fail"

    # Grade system
    if marks > 90:
        grade = "A"
    elif marks > 75:
        grade = "B"
    elif marks > 50:
        grade = "C"
    else:
        grade = "F"

    print(f"{name} -> Marks: {marks}, Status: {status}, Grade: {grade}")

# Final calculations
average = total / n

print("\n--- Summary ---")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Topper: {topper} ({highest_marks})")
print(f"Lowest: {lowest_student} ({lowest_marks})")
print(f"Students Passed: {pass_count}/{n}")