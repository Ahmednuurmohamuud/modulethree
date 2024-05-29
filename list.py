list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list2 = [21, 22, 23]

list1.sort()
print(list1)


add = list1 + list2
print(add)


add.sort()
print(add[18:23])
print(add[0:3])


for  number in add:
     if number %2 == 0:
         add.remove(number)


print(add)

