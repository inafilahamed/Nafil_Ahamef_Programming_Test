'''Problem-2: With a single integer as the input, generate the following until
a = x [series of numbers as shown in below examples]'''

n = int (input('enter the number:'))
series = [2*i-1 for i in range(1,n+1)]
print('series of numbers are:',series)

'''
output:
enter the number:5
series of numbers are: [1, 3, 5, 7, 9]

Process finished with exit code 0'''