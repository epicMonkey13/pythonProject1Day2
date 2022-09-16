#slicing
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
xyz = ['a', 'b', 'c', 'd']
print(list[:])
print(list[2:])
print(list[:4])
print(list[2:7])
print(list[1:10:5])
print(list[::2]) # if starts with odd give odd
#negative slicing
print(list[-3:])
print(list[-7:-3])
print(list[::-1]) #reversing
print(xyz[::-1])

#slicing lists
a = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh"]
print("The Actual List is this: ", a)
print("The Sliced List is : ")
b = a[:3] + a[6:]
print(b)
c = a[::2]+a[1::2]
print("The modified list is : ", c)
# stack overflow help
# a[-1]    # last item in the array
# a[-2:]   # last two items in the array
# a[:-2]   # everything except the last two items
# a[::-1]    # all items in the array, reversed
# a[1::-1]   # the first two items, reversed
# a[:-3:-1]  # the last two items, reversed
# a[-3::-1]  # everything except the last two items, reversed




