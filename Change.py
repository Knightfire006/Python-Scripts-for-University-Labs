"""creates a class to create our money objects"""
class Money:
    def __init__(self, singular_name, plural_name, value):
        self.singular_name = singular_name
        self.plural_name = plural_name
        self.value = value
"""initializes our money with  singular and plural names and its value amount"""
dollar = Money("Dollar", "Dollars", 100)
quarter = Money("Quarter", "Quarters", 25)
dime = Money("Dime", "Dimes", 10)
nickel = Money("Nickel", "Nickels", 5)
penny = Money("Penny", "Pennies", 1)

"""
-since each money requires the same math, its easier to create a function and call then repeat the code
-each cycle of the while loop subtracts the money amount and then count increases. less code than using % and // together
-once the subtraction from the amount would result in a negative number it breaks the while loop.
-it prints the count of money for change then returns the remaining amount of money.
"""
def change_calculator(amount, divider):
    """keeps track of how many times each type of money can go into the amount"""
    count = 0
    while ((amount - divider.value) >= 0):
        count += 1
        amount -= divider.value
    else:
        if count > 0:
            if count >= 2: #checks to see if multiple of the money for change
                print("{} {}".format(count, divider.plural_name))
            else:
                print("{} {}".format(count, divider.singular_name))
        return amount #returns the remaining amount of money after change subtracted

"""

**************Begining of program*****************

"""


total_amount = int(input())

if total_amount > 0:#checks to make sure there is a need for change
    """amount decreases as each money is process through the function"""
    amount = change_calculator(total_amount, dollar)
    amount = change_calculator(amount, quarter)
    amount = change_calculator(amount, dime)
    amount = change_calculator(amount, nickel)
    amount = change_calculator(amount, penny)
else:
    print("No change")

























