from decimal import Decimal, getcontext

from long_number_probability_calculator import constants as c

getcontext().prec = c.DP

def calculate(n: int, m: int, d: int) -> float:
    """Calculates the probabilty that number m appears at least once within number n"""

    n = Decimal(n)
    m = Decimal(m)
    d = Decimal(d)

    k = n-m+1
    neg_m = m*-1
    P = 1-(1-d**neg_m)**k

    return format(P, "f")