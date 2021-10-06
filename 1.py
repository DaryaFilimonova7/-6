delta = int(input("Введите значение delta: "))

print("Введите элементы массива: ")
a = int(input())
array = []
while True:
    try:
        array.append(a)
        a = int(input())
    except:
        break
minimum = min(array)
element = minimum + delta
k = 0
for i in array:
    if i == element:
        k = k + 1 
    else:
        continue

print("Количество элементов, отличающихся от минимального на delta, равно " + str(k))