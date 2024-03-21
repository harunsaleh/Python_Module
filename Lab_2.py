#A software company sells a package that retails for $100. Quantity discounts are given according to the following table:
#                          Quantity                Discount
#                         10–20                   10%
#		                  21–50                   20%
#                         51–100                  25%
#                         Greater than 100        30%
#
#Write a program that asks the user to enter the number of packages purchased. Ensure the quantity input is a positive number. The program should then display the amount of the discount (if any) and the total amount of the purchase after the discount.

retail = 100
while True:
    try:
        quantity = int(input("Enter a quantity amount: "))
        assert(quantity > 0), "Quantity must be bigger than 0"

        if 10 <= quantity <= 20:
            discount_rate = 0.10
        elif 21 <= quantity <= 50:
            discount_rate = 0.20
        elif 51 <= quantity <= 100:
            discount_rate = 0.25
        elif quantity > 100:
            discount_rate = 0.30
        else:
            discount_rate = 0  # For quantities less than 10, no discount

        quantity_retail = retail * quantity
        quantity_discount = quantity_retail * discount_rate
        final_price = quantity_retail - quantity_discount

        if discount_rate > 0:
            print(f"Your quantity qualifies for a discount of: {discount_rate*100}%. "
                  f"The price after discount is: {final_price}$")
        else:
            print(f"The price for the quantity is: {final_price}$")
        break

    except AssertionError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please try again!")
