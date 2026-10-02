# List and Tuple|


marks = [94.1,98,89.2,96,78]

print(marks)
print(type(marks))
print(len(marks))

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])


# in python strings are immutable and lists are mutable

names =["Arslan ", "Wali"]


names[0]="KHan"

print(names)

#list sclicing 

list = [1,2,3,4,5,6,7,8,9,10]

print (list[1:2])

print(list[:-3])

#list method 

list1=[3,1,2,5,6]

list1.append(4)
print(list1)


list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

print(list1.reverse())

