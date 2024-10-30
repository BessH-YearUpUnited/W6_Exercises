calc_dict = {
    'plus': lambda n1, n2: n1 + n2,
    'minus': lambda n1, n2: n1 - n2,
    'times': lambda n1, n2: n1 * n2,
    'divide': lambda n1, n2: n1 / n2
}

print(calc_dict['divide'](24, 2))
print(calc_dict['times'](12, 3.0))


def discount_calculator(pct_off):
    return lambda price: price * (1 - pct_off)

discount20 = discount_calculator(.2)
discount25 = discount_calculator(.25)

price = float(input("Enter price: "))

print(f'A 20% discount on {price} is {round(discount20(price),2)}')
print(f'A 25% discount on {price} is {round(discount25(price),2)}')