# Procedure programming structures code into procedures, sometimes called subroutines or functional sections of code. Procedural programming allows for DRY (Don't Repeat Yourself) principle.
# Procedural code are easy to write and understand. They are highly reusable. Some of the disadvantages are - hard to maintain, doesn't relate well, data is exposed throughtout the whole program.


def billTotal(bill):
    total = 0
    for k, v in bill.items():
        total += v
    return total


def calculateTax(billTotal, percent):
    return round((billTotal * percent) / 100, 2)


foodBill = {1: 3.99, 2: 4.55, 3: 11.99, 4: 22.00, 5: 2.00}

footTotal = billTotal(foodBill)
taxTotal = calculateTax(footTotal, 15)

print("Overall:", footTotal + taxTotal)
