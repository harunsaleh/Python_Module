#Write code that does the following:
#Create an an output file with the filename list.txt that uses a loop to write numbers 1 through 20 to the file, then closes the file.
#Then have your code open the list.txt file and then read all of the numbers from the file to then display each number one line at a time to the console then closes the file.
#Use exception handling where applicable.

def create_file():
    try:
        file = open("lab5_list.txt", "w")
        for x in range(1,21):
            file.write(str(x) + "\n")
            print(f"Number: {x} added to the file")
    except IOError as e:
        print(f"An error occurs while creating or writing the file {e}")
    finally:
        file.close()

def open_file():
    try:
        file = open("lab5_list.txt", "r")
        print("Now we are reading the lines:\n", file.read())
    except IOError as e:
        print(f"An error occurs while opening or reading the file: {e}")
    finally:
        file.close()

create_file()
open_file()
