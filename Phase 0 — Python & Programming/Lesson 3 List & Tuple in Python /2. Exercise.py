#WAP to ask the user to enter names of their 3 facorite movies and store them in a list


print("Entery Your Favorite Movies Names")
mov1=str(input("Enter Your 1st Move "))
mov2=str(input("Enter Your 2nd Move "))
mov3=str(input("Enter Your 3rd Move "))

movies=[mov1,mov2,mov3]

print(movies)

#Palliandorm

list5=[1,2,1]

copy_list=list5.copy()

copy_list.reverse()

if copy_list==list5:
    print("Palliandorm")

else:
    print("not palliandorm")


#WAP to; count the number of students with the "A" grade in the foloing tuple
tuup=("C","A","A","B","C","A")

print(tuup.count("A"))

#store the above values in a list and sort them from "A" to "D"

grades=["C","A","A","B","C","A"]

grades.sort()

print(grades)