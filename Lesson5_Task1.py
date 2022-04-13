#вывести первые N чисел кратные M и больше K

#import sys

print('введите число M')
m = int(input())
print('введите число K')
k = int(input())
print ('введите ограничение на количество выводимых чисел')
n = int(input())
for i in range(k+n*m):
    if i % m == 0 and i > k:
        print(i, end=' ')
