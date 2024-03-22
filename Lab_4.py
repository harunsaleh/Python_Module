def letter_grades(average): #Transforming students test scores to GPA
    if 1.0 <= average <= 1.5:
        return "GPA: A"
    elif 1.6 <= average <= 2.5:
        return "GPA: B"
    elif 2.6 <= average <= 3.5:
        return "GPA: C"
    elif 3.6 <= average <= 4.5:
        return "GPA: D"
    else:
        return "GPA: F"

def calculate_average(): #Input of students test scores
    scores = []
    for i in range (1, 6):
        score = int(input(f"Please enter score {i}: "))
        scores.append(score)
    average = sum(scores) / len(scores)
    print("Your entered scores are:", scores)
    print("Average score is:", average)
    grade = letter_grades(average)
    print(grade)

calculate_average()
