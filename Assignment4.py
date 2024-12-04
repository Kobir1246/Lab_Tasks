# a. Categorize each student's grade using if-else and display their grade category
def categorize_grades(grades):
    print("Grade Categories:")
    for score in grades:
        if score > 80:
            grade = 'A'
        elif 60 <= score <= 80:
            grade = 'B'
        elif 40 <= score <= 60:
            grade = 'C'
        else:
            grade = 'F'
        print(f"Score: {score} - Grade: {grade}")

# b. Implement boost_grades function to increase grades by 5%
def boost_grades(grades):
    return list(map(lambda x: round(x * 1.05, 2), grades))  # Round to 2 decimal places

# c. Use lambda to find which boosted grades are now above 90
def find_boosted_above_90(boosted_grades):
    return list(filter(lambda x: x > 90, boosted_grades))

# Initial grades array
grades = [85, 78, 92, 45, 33, 67, 88, 41]

# Call the function to categorize grades
categorize_grades(grades)

# Boost the grades by 5% and round to 2 decimal places
boosted_grades = boost_grades(grades)
print("\nBoosted Grades:")
print(boosted_grades)

# Find and print grades above 90
boosted_above_90 = find_boosted_above_90(boosted_grades)
print("\nBoosted Grades Above 90:")
print(boosted_above_90)
