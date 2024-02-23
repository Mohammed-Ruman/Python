# 9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

cost_unit=int(input("Enter Cost per Unit? "))

quantity=int(input("Enter Quantity? "))

total_cost=cost_unit*quantity

if total_cost > 1000:
    total_cost = total_cost - total_cost*0.1

print(total_cost)

