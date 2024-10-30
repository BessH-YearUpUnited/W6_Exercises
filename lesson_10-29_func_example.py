current_time = '1:28 PM'

def stopwatch(m, s):
    time_result = f'{m}:{s}'
    print(f'Current time is: {current_time}')
    return f'Time result is {time_result}'

print(f'Result from stopwatch: {stopwatch(1, 12)}')
print(f'Result from stopwatch: {stopwatch(0, 48)}')







# def my_first_function():
#     print("Hello world!")
#     return "How are you?"

# print(my_first_function())


# def calculator(n1, n2, operation = 'plus'):
#     print(f'Input values are {n1} and {n2}')
#     print(f"You have chosen the {operation} operation")
#     if operation == 'minus':
#         return f'Your result is {n1 - n2}'
#     elif operation == 'times':
#         return f'Your result is {n1 * n2}'
#     elif operation == 'divide':
#         return f'Your result is {n1 / n2}'
#     else:
#         return f'Your result is {n1 + n2}'

# print(calculator(n2=23, n1=2, operation='minus'))


# # print(calculator(35, 871, 'divide'))

# # def calculator2(*nums):
# #     return nums

# # print(calculator2(2,4,6,8))

# # def guest_list(*args):
# #     return f'The guest list includes: {args}'

# # print(guest_list('Michael'))

# # def relative(name, relationship):
# #     return f'{name} is my {relationship}'

# # print(relative(relationship='cousin', name='Becky'))

# def rels(rel, name, **kwargs):
#     kwargs['relationship'] = rel
#     kwargs['name'] = name
#     print(kwargs)

# print(rels('cousin', 'Becky', address='103 Maple', city_state_zip='West Chicago, IL 60188'))
