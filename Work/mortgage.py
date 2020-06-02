# mortgage.py
#
# Exercise 1.7
# mortgage.py

from dataclasses import dataclass

@dataclass
class Mortgage:
    principal: float
    payment: float
    total_paid: float
    total_months: int
    first_12: bool

def mortgage_calc(principal, payment, total_paid, total_months, first_12=False):
    rate = .05
    if first_12:
        payment = 3684.11
    while principal > 0:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        total_months += 1
        if total_months == 12 and first_12:
            return Mortgage(principal, payment, total_paid, total_months, first_12)
    return Mortgage(principal, payment, total_paid, total_months, first_12)

def main():
    principal = 500000.0
    payment = 2684.11
    total_paid = 0.0
    mortgage1 = mortgage_calc(500000.0, 3684.11, 0.0, 0, first_12=True)
    mortgage2 = mortgage_calc(mortgage1.principal, 2684.11, mortgage1.total_paid, mortgage1.total_months, first_12=False)
    print('Total Payment: ', round(mortgage2.total_paid, 2))
    print('Total Months: ', mortgage2.total_months)

if __name__ == '__main__':
    main()
