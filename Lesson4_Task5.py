import collections
print("введите список чисел через пробелы")
spisok = list(map(int, input().split()))
data = collections.Counter(spisok)
data = data.values()
print(data)




