# Exercise

# WAP to check if a number entered by the user is odd or even

num=int(input("Enter Your Number to Check Even or Odd"))

if num%2==0:
    print("Even")
else:
    print("Odd")


#WAP To find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter your 1st number"))
num2= int(input("Enter your 2nd number"))
num3 = int(input("Enter your 3rd number"))

if (num1>=num2 and num1>=num3):
    print("num1 is greater")
elif (num2>=num1 and num2>=num3):
    print("num2 is greater")
else:
    print("num3 is greater")

    