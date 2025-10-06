print(" SECTION A: Initial Setup - Scalar Objects and Loops ")

# 1. Ask number of students
num_students = int(input("Enter number of students: "))

students = []  # List to store (name, grade)

# 2. Input student names and grades
for i in range(num_students):
    name = input(f"\nEnter name of student {i + 1}: ")

    # 3. Validate grade input (0–100)
    while True:
        try:
            grade = float(input(f"Enter {name}'s grade (0–100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Invalid grade.Please re-enter your grade.")
        except ValueError:
            print("Please enter a numeric value.")

    students.append((name, grade))  # Store as tuple (name, grade)

# 4. Calculate total and average
total = sum(grade for _, grade in students)
average = total / num_students

# 5. Display results
print("\nClass Summary")
for name, grade in students:
    print(f"{name}: {grade}")

print(f"\nClass Average: {average:.2f}")

