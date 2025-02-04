lakh = 100000
from sys import maxsize

new_regime_2526 = [
    [0, 4*lakh, 0],
    [4*lakh, 8*lakh, 0.05],
    [8*lakh, 12*lakh, 0.10],
    [12*lakh, 16*lakh, 0.15],
    [16*lakh, 20*lakh, 0.20],
    [20*lakh, 24*lakh, 0.25],
    [24*lakh, maxsize, 0.30],
]

new_regime_2425 = [
    [0, 3*lakh, 0],
    [3*lakh, 7*lakh, 0.05],
    [7*lakh, 10*lakh, 0.10],
    [10*lakh, 12*lakh, 0.15],
    [12*lakh, 15*lakh, 0.20],
    [15*lakh, maxsize, 0.30],
]

def get_tax(income: int, taxbracket: list[list[int]], rebate: int, standard_deduction: int = 75000):
    tax = 0
    income -= standard_deduction
    
    if income <= rebate: return 0

    for bracket in taxbracket:
        lb=bracket[0]
        rb=bracket[1]
        p=bracket[2]

        if income > lb and income > rb:
            tax += (rb - lb)*p
        if income >lb and income <= rb:
            tax += (income - lb)*p
    
    return tax