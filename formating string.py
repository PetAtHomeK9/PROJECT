price_of_a_house = 1000000

buyer_has_good_credit = True

if buyer_has_good_credit:
    down_payment = 0.1 * price_of_a_house
else:
    down_payment = 0.2 * price_of_a_house
print(f"Down payment: {down_payment}")