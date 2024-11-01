print("Filled in steps from in-class demo")

def numbers(*num):
    return num

result = numbers(2, 4, 6, 8)

result_list = ''

for i in result:
    result_list = result_list + str(i)
    if i == result[-1]:
        break
    else:
        result_list = result_list + ' + '

sum_result = 0

for n in result:
    sum_result += n

print(f'{result_list} = {sum_result}')


# # #
# # #
# # #

print("Essentially the same steps, but all wrapped into the function")

def numbers2(*num):

    result_list2 = ''

    for i in num:
        result_list2 = result_list2 + str(i)
        if i == num[-1]:
            break
        else:
            result_list2 = result_list2 + ' + '
    
    sum_result2 = 0

    for n in num:
        sum_result2 += n

    return f'{result_list2} = {sum_result2}'

print(numbers2(3, 5, 7, 9))
