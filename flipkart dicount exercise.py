# This program is about giving a discount to the flipkart users for buying a cell phone in 2 different cases
    # 1. if they pay the bill through google pay, give them 20% dicount
    # 2. or else, give them 10% discount#

mobile_price = 9500

is_google_pay = True

if is_google_pay:
    discount = 0.2 * mobile_price
    total_price = mobile_price-discount

else:
    discount = 0.1 * mobile_price

print(f"Discount Amount : {discount}")
print(total_price)
