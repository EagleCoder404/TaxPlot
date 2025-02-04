"""Has all the tax bracket data"""

from sys import maxsize
LAKH = 100000

NEW_REGIME_2024 = [
    [0, 3*LAKH, 0],
    [3*LAKH, 7*LAKH, 0.05],
    [7*LAKH, 10*LAKH, 0.10],
    [10*LAKH, 12*LAKH, 0.15],
    [12*LAKH, 15*LAKH, 0.20],
    [15*LAKH, maxsize, 0.30],
]

NEW_REGIME_2025 = [
    [0, 4*LAKH, 0],
    [4*LAKH, 8*LAKH, 0.05],
    [8*LAKH, 12*LAKH, 0.10],
    [12*LAKH, 16*LAKH, 0.15],
    [16*LAKH, 20*LAKH, 0.20],
    [20*LAKH, 24*LAKH, 0.25],
    [24*LAKH, maxsize, 0.30],
]
