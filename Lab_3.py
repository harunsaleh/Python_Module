#Given tuition for a full-time student is $5,000 per semester,
#your program should show the increase in tuition if the tuition will increase by 4 percent each year
#over the next 5 years. Have your code use a loop that will display the projected semester tuition amount
#for the next 5 years.
#Display the year for each iteration of your loop as well.

tuition = 5000
for year in range(1,6):
    tuition = tuition + tuition * 0.04
    print(f"For Year {year}: {tuition:.2f}")
