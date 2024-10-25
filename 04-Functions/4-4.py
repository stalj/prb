def sum_digits(number):
    str_num = str(number)
    sum = 0
    for i in str_num:
        number_new=int(i)
        sum = sum +number_new 
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(abs(any_number))
print(f'The sum of the digits in the number {any_number} is {result}')