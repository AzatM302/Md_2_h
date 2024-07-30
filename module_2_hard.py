numbers = range(3, 21)
i = 0
while i < len(numbers):
    first_numbers = numbers[i]
    i += 1
    result = ''
    for j in range(1, 20):
        for k in range(j + 1, 20):
            if first_numbers % (j + k) == 0:
                result += str(j) + str(k) + str(i)
    print(f'{first_numbers} - {result}')
