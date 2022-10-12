# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

S = 'DDDDDHHHHHHHKKKKKKKKKLLLLLLLLLLLLLLL'
print(S)

lst =[]
t= None
for i in S:
    if i != t:
        lst.append(i)
        lst.append(str(1))
        t = i
    else:
        lst[-1] = str(int(lst[-1]) + 1)
print("".join(lst))


