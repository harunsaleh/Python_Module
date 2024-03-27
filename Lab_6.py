#Write a program that creates a dictionary containing any 5 U.S. states as keys, and their capitals as values.
#(Use the Internet to get a list of your chosen states and their capitals.)
#The program should quiz the user by displaying the name of each state
#and asking the user to enter that state’s capital.
#The program should keep a count of the number of correct and incorrect responses.

dictionary = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento"
}
countwrong = 0
countcorrect = 0

for i in dictionary:
    print("Number of correct answers:", countcorrect)
    print("Number of wrong answers:", countwrong, "\n")
    print("What is the capital of", i)
    answer = input(str("Enter your answer: "))
    if answer == dictionary[i]:
        print("Correct!")
        countcorrect += 1
    else:
        print("Incorrect!")
        countwrong += 1
print("You got", countcorrect, "correct answers and", countwrong, "wrong answers.")
