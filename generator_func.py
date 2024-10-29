# def calculator1(n1, n2):
#     return n1 + n2

# print(calculator1(34,25))

def calculator2(n1, n2):
    yield n1 + n2
    yield "Do you want to calculate another set of numbers?"
    y_n = input("Y or N").upper()
    yield f"You responded {y_n}"


for x in calculator2(17,8):
    print(x)


