# cars = ["BMW", "BENZ", "KIA"]
# cars.append("AUDI")
# print(cars)
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# a.append(b)
# print(a)
#
# #clear method
# var = [1, 1, 12, 45]
# var1 = ["pen", "ball", "ink"]
# var2 = ["!", "@", "$"]
# var.clear()
# var2.clear()
# print(var)
# print(var1)
# print(var2)

#copy method
# x = [1, 2, 3, 4]
# y = x.copy()
# z = y
# print(z)
#
# # second copy method
# instruments = ["piano", "violin"]
# instruments1 = instruments.copy() #method 1
# xyz = instruments1 #method 2
# print(xyz)

#count method
# cars = ["audi", "maruti", "kia", "ford", "hyundai", "bmw", "hyundai"]
# num = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
# var1 = num.count(1)
# var2 = num.count(2)
# var = cars.count("hyundai")
# print(var)
# print(var1)
# print(var2)


#insert method
# xyz = ["USA", "India", "UK"]
# #usa index 0
# #india index 1
# #uk index 2
# xyz.insert(1, "Europe")
# xyz.insert(4, "Austria")
# print(xyz)

#extend
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = [11, 12, 13, 14, 15, 16]
# x.extend(y)
# # x.append(y) #appends as a nested list
# print(x)

#pop
# xyz = ["apple", "banana", "cherry", "berries"]
# # xyz.pop() #no index number  - deletes the last one
# xyz.pop(0)
# # print(xyz)
# print(len(xyz)) #prints 3


#remove
# abc = ["cars", "fruits", "accessories", "appliances"]
# abc.remove("cars") #must say what to remove
# print(abc)

#reverse
# aaa = ["a", "b", "c", "d"]
# aaa.reverse()
# print(aaa)
#
# x = aaa.index("c")
# print(x)

#sort method
# a = ["volvo", "banana", "watch", "electric gadgets", "apple"]
# a.sort()
#  #sorts the list in an alphabethical order
# a.sort(reverse=False) #can say True here as well
# print(a)

#additional methods self-practice

#fromkeys
# x = ('key1', 'key2', 'key3')
# y = 0
#
# thisdict = dict.fromkeys(x, y)
#
# print(thisdict)

#get
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.get("model")
#
# print(x)

#exercises from w3schools

# fruits = ["apple", "banana", "cherry"]
# print(fruits[1])

#Change the value from "apple" to "kiwi", in the fruits list.
# fruits = ["apple", "banana", "cherry"]
# fruits[0] = "kiwi"
# print(fruits)

#Use the append method to add "orange" to the fruits list.
# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# print(fruits)

#Use the insert method to add "lemon" as the second item in the fruits list.
# fruits = ["apple", "banana", "cherry"]
# fruits.insert(1, "lemon")
# print(fruits)

#Use the remove method to remove "banana" from the fruits list.
# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")
# print(fruits)

#Use negative indexing to print the last item in the list.
# fruits = ["apple", "banana", "cherry"]
# print(fruits[-1])


















