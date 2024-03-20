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
                  f"The price after discount is: {final_price}")
        else:
            print(f"The price for the quantity is: {final_price}")
        break

    except AssertionError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please try again!")
