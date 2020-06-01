# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0


def mortgage_calc(principal, payment, total_paid, first_12=False):
    total_months = 0
    while principal > 0:
        if first_12:
            while principal > 0:
                # print('s')
                principal = principal * (1+rate/12) - 3684.11
                total_paid = total_paid + 3684.11
                total_months += 1
                if total_months == 12:
                    return total_paid, total_months, principal
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        total_months += 1
    return total_paid, total_months

first = mortgage_calc(500000.0, 3684.11, 0.0, first_12=True)
print(first)
second = mortgage_calc(first[-1], 2684.11, first[0], first_12=False)
print(second)

print('Total paid: ', total_paid)
print('Total months: ', total_months)
