#       Student Report Card Generator


studMarks={}

subjects=["Tamil","English","Mathematics","Science","Social Science"]

id=int(input("Enter your ID:"))
name=input("Enter your Name:")
grade=""

total=0
for sub in subjects:
    marks=int(input("Enter the Mark of "+sub+" : "))

    while marks>100 or marks<0:
        print("Invalid Input! \nPlease Enter the Mark again.")
        marks=int(input("Enter the Mark of "+sub+" : "))
    studMarks[sub]=marks
    total=total+marks

avg=total/5

if(avg>=90):
    grade="A"

elif(avg>=80):
    grade="B"

elif(avg>=70):
    grade="C"

elif(avg>=60):
    grade="D"

else:
    grade="F"
    
print()
print("----REPORT CARD----\n")
print("ID:",id)
print("Name:",name)
print()
for key, value in studMarks.items():
    print(key+" : "+str(value))
print()
print("Total Marks:",total)
print("Grade:",grade)