# 12. Calculate income tax
# Calculate income tax for the given income by adhering to the rules below
#
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20

def calculate_tax(amt):
    if amt <= 10000:
        tax = amt * 0
        return tax
    elif  20000 >= amt > 10000:
        tax = 10000 * 0 + ((amt - 10000) * 0.1)
        return tax
    else:
        tax = 10000 * 0
        tax += 10000 * 0.1
        tax += (amt - 20000) * 0.20
        return tax

income = int(input("Enter your income: "))
print(f"Tax payable: {calculate_tax(income)}")