def calculate_grade(marks):
    marks = float(marks)

    if marks >= 90:
        return "O", "Outstanding performance. Keep up this remarkable consistency."
    elif marks >= 80:
        return "A+", "Excellent work. You are very close to the top."
    elif marks >= 70:
        return "A", "Great job. Your effort is clearly visible."
    elif marks >= 60:
        return "B+", "Good performance. A little more focus can take you higher."
    elif marks >= 50:
        return "B", "Decent work. Keep practicing and improving."
    else:
        return "C", "Do not be discouraged. Use this opportunity to learn and grow."

print("=== Student Grade Calculator ===\n")

marks = input("Enter the marks (0–100): ").strip()

while not marks.replace('.', '', 1).isdigit() or float(marks) < 0 or float(marks) > 100:
    marks = input("Please enter a valid number between 0 and 100: ").strip()

grade, message = calculate_grade(marks)

print("\n------------------------------------")
print(f"Marks: {marks}")
print(f"Grade: {grade}")
print(message)
print("------------------------------------")
