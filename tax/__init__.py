"""Contains all the \"fun\" tax logic :)"""

def get_tax(
        income: int,
        taxbracket: list[list[int]],
        rebate: int,
        standard_deduction: int = 75000
        ) -> int:
    """Returns tax for given income"""

    tax = 0
    income -= standard_deduction
    if income <= rebate:
        return 0
    for bracket in taxbracket:
        lb=bracket[0]
        rb=bracket[1]
        p=bracket[2]

        if income > lb and income > rb:
            tax += (rb - lb)*p
        if income >lb and income <= rb:
            tax += (income - lb)*p
    return tax
