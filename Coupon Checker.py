# -----------------------------------------------------
# Coupon Checker Program
# Purpose:
#   - Use boolean values and operators
#   - Use all six comparison operators
#   - Use if, elif, else for flow control
# -----------------------------------------------------

# Inputs
price = float(input("Enter the price of your item: "))
coupon_value = float(input("Enter your coupon amount: "))
expiration_days = int(input("How many days until the coupon expires? "))

# Boolean expressions
coupon_not_expired = expiration_days > 0      # coupon valid only if more than 0 days remain
coupon_big_enough = coupon_value <= price     # coupon can’t be bigger than the price

# Comparison operator examples
print("\nComparisons:")
print("Is the coupon expired?", expiration_days == 0)
print("Is the price NOT $0?", price != 0)
print("Is the price greater than $20?", price > 20)
print("Is the coupon value less than $5?", coupon_value < 5)
print("Is the price greater or equal to 10?", price >= 10)
print("Is the coupon value less or equal to the item price?", coupon_value <= price)

# Flow control
print("\nResult:")
if coupon_not_expired and coupon_big_enough:
    print("Your coupon can be used!")
elif not coupon_not_expired:
    print("You can't use the coupon because it has expired.")
elif not coupon_big_enough:
    print("You can't use the coupon because it is larger than the item price.")
else:
    print("Something went wrong. Please try again.")
