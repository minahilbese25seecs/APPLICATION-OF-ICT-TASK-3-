marks =int(input("ENTER YOUR MARKS:"))

if marks>=90 and marks<=100:
    grade="A"
elif marks>=80 and marks>=75:
    grade="B"
elif marks<=75 and marks>=60:
    grade="C"
elif marks<=60 and marks>=50:
    grade="D"
elif marks<=30 and marks<50:
    grade="F"
else:
    print("invalid")

print("GRADE: ",grade)


    