#Steps to Complete This Project
#STEP 1	Open MS Visual Studio Code and create your first program!
#Open MS Visual Studio Code for Python and create a file in Visual Studio Code (VSC). will allow you to enter your source code in an editor style format like Notepad or TextEdit if you are on a Mac.
#Have your program perform the following logic:
#Using Python operators and variable declarations
#In your editor, you may begin typing your source code. Write code that asks the user to enter the projected amount of total sales, then display the profit that will be made from that amount. Hint: Calculate profit to be 0.23 (or 23 percent) of sales.
#STEP 2	Run your program
#To run your program, choose the Run  icon within your editor.  Check your output results for accuracy!


sales = input("Please enter the amount of total sales: ")
sales = float(sales) * 0.23
print(sales)
