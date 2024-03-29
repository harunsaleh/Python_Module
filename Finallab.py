#Write a GUI program that calculates a car’s gas mileage. The program’s window should have Entry widgets that let the user enter the number of gallons of gas the car holds, and the number of miles it can be driven on a full tank. When a Calculate MPG button is clicked, the program should display the number of miles that the car may be driven per gallon of gas. Use the following formula to calculate miles-per-gallon:

#		           MPG = miles / gallons
import tkinter
import tkinter.messagebox

class CarMPG:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter the number of gallons of gas the car holds:')
        self.gallons_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack the top frame's widgets.
        self.prompt_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        # Create the widgets for the middle frame.
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter the number of miles the car can be driven on a full tank:')
        self.miles_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack the middle frame's widgets.
        self.prompt_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate MPG', command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    def calculate(self):
        # Get the values entered by the user.
        gallons = float(self.gallons_entry.get())
        miles = float(self.miles_entry.get())

        # Calculate the MPG.
        mpg = miles / gallons

        # Display the result in an info dialog box.
        tkinter.messagebox.showinfo('Results', 'The MPG is ' + format(mpg, ',.2f'))
# Create an instance of the CarMPG class.
car_mpg = CarMPG()
