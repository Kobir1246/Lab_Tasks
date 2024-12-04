def manage_courses():
    # Step 1: Create the initial dictionary with given courses
    courses = {
        "CSE101": {"Course name": "Introduction to Programming", "Credits": 3, "Instructor": "Dr. Alice"},
        "CSE102": {"Course name": "Data Structures", "Credits": 4, "Instructor": "Dr. Bob"},
        "CSE103": {"Course name": "Database Systems", "Credits": 3, "Instructor": "Dr. Carol"}
    }
    
    # Step 2: Update the instructor's name for CSE102
    courses["CSE102"]["Instructor"] = "Dr. Bob Jr."
    
    # Step 3: Add a new course
    courses["CSE104"] = {"Course name": "Algorithms", "Credits": 4, "Instructor": "Dr. Dave"}
    
    # Step 4: Remove the course CSE101
    if "CSE101" in courses:
        del courses["CSE101"]
    
    # Step 5: Loop through the dictionary and print the course code along with its details
    for code, details in courses.items():
        print(f"Course Code: {code}")
        for key, value in details.items():
            print(f"  {key}: {value}")
        print()  # Add a blank line for readability

# Call the function to perform the operations
manage_courses()
