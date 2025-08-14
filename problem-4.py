'''Problem-4: Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]'''

numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
multiplies_count = {}

for i in range(1,10):
    count = 0
    for num in numbers:
        if num % i == 0:
            count += 1
        multiplies_count[i] = count
print('output:',multiplies_count)

'''
output: {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}

Process finished with exit code 0'''