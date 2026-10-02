

#Condtional Statement 


age= 21

if (age >=18):
    print("You are eligble for vote")
else:
    print("You are not eligble for vote")


light = "green"

if (light == "green"):
    print("Go") #indetation
elif (light == "yellow"):
    print("Wait")
else:
    print("Stop")


#Grade Student Based on Marks

marks = 90

if (marks>=90):
    print("Grade A")
elif (marks>=80 and marks<90):
    print("Grade B")
elif (marks>=70 and marks>80):
    print("Grade C")
elif (marks>=60 and marks>60):
    print("Grade D")
else:
    print("Fail")

# Nesting

age = 34

if (age>=18):
    if (age>80):
        print("can't  drive")
    else:
        print('can drive')
else:
    print('Cant Drive')