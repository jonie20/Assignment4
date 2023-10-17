def grade_system(marks):

  if marks < 0 or marks > 100:
    return "Invalid marks"
  elif marks >= 0 and marks < 31:
    return "D"
  elif marks >= 31 and marks < 51:
    return "C"
  elif marks >= 51 and marks < 71:
    return "B"
  elif marks >= 71 and marks <= 100:
    return "A"
  else:
    return "Invalid marks"


# Get the marks from the user
marks = int(input("Enter the marks: "))

# Calculate the grade
grade = grade_system(marks)

# Print the grade
print("Grade:", grade)
