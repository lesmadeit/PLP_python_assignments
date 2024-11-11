def calculate_discount(price, discount_percent):
    # Check if discount percent is 20 or higher
    if discount_percent >= 20:
        # Calculate discount amount and final price
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return original price
        return price

# Prompt the user for the original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price using the function
    final_price = calculate_discount(price, discount_percent)

    # Display the result
    if final_price == price:
        print("No discount applied. The price remains:", final_price)
    else:
        print("The final price after discount is:", final_price)
except ValueError:
    print("Please enter a valid number for price and discount percentage.")







