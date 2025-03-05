# Function to calculate the average marks for a subject
def calculate_subject_average(assignment, coursework, mid_term, end_of_term):
    return (assignment + coursework + mid_term + end_of_term) / 4

# Function to calculate the overall average across all subjects
def calculate_overall_average(physics_avg, chemistry_avg, math_avg):
    return (physics_avg + chemistry_avg + math_avg) / 3

print("Enter marks for Physics:")
physics_assignment = float(input("Assignment: "))
physics_coursework = float(input("Coursework: "))
physics_mid_term = float(input("Mid-term Exam: "))
physics_end_of_term = float(input("End-of-term Exam: "))

print("\nEnter marks for Chemistry:")
chemistry_assignment = float(input("Assignment: "))
chemistry_coursework = float(input("Coursework: "))
chemistry_mid_term = float(input("Mid-term Exam: "))
chemistry_end_of_term = float(input("End-of-term Exam: "))

print("\nEnter marks for Math:")
math_assignment = float(input("Assignment: "))
math_coursework = float(input("Coursework: "))
math_mid_term = float(input("Mid-term Exam: "))
math_end_of_term = float(input("End-of-term Exam: "))

# Calculate averages for each subject
physics_avg = calculate_subject_average(physics_assignment, physics_coursework, physics_mid_term, physics_end_of_term)
chemistry_avg = calculate_subject_average(chemistry_assignment, chemistry_coursework, chemistry_mid_term, chemistry_end_of_term)
math_avg = calculate_subject_average(math_assignment, math_coursework, math_mid_term, math_end_of_term)

# Calculate overall average
overall_avg = calculate_overall_average(physics_avg, chemistry_avg, math_avg)

print("\nResults:")
print(f"Physics Average: {physics_avg:.2f}")
print(f"Chemistry Average: {chemistry_avg:.2f}")
print(f"Math Average: {math_avg:.2f}")
print(f"Overall Average: {overall_avg:.2f}")
