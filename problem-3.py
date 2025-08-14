'''Problem-3: With a single integer as the input, generate the following until
 a = x [series of numbers as shown in below examples]'''

n = int(input("Enter a number: "))

if n % 2 == 0:
    series_len = n - 1
else:
    series_len = n

series = [2*i - 1 for i in range(1, series_len+1)]
print('series output:',series)

'''
output: 
Enter a number: 6
series output: [1, 3, 5, 7, 9]

Process finished with exit code 0'''