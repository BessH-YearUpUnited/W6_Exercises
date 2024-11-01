print("Filled in steps from in-class demo")

def numbers(*num):
    return num

result = numbers(2, 4, 6, 8)

result_list = ''

for i in result:
    print(i)
    result_list = result_list + str(i)
    if i == result[-1]:
        break
    else:
        result_list = result_list + ' + '

print(result_list)

sum_result = 0

for n in result:
    sum_result += n

print(f'{result_list} = {sum_result}')



# # #

# print("Same steps, but wrapped in function")


# # Work in progress!
# def numbers2(*num):
#     return num

# result = numbers(2, 4, 6, 8)

# result_list = ''

# for i in result:
#     print(i)
#     result_list = result_list + str(i)
#     if i == result[-1]:
#         break
#     else:
#         result_list = result_list + ' + '

# print(result_list)

# sum_result = 0

# for n in result:
#     sum_result += n

# print()
