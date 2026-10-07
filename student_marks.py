name = input("Enter your name")
subject1 = int(input("Enter Subject 1 marks:"))
subject2 = int(input("Enter Subject 2 marks:"))
subject3 = int(input("Enter Subject 3 marks:"))
total = subject1 + subject2 + subject3
Average = total / 3
print("name:", name)
print("Average:", Average)
print("total:", total)
if Average >= 35:
    print("Result: pass")
else:
    print("Result: fail")     
if Average >=90:
    grade = "A"    
elif Average >=75:
    grade = "B"   
elif Average >= 60:
    grade = "C"    
elif Average >= 35:
    grade = "D"
else:
    grade = "F"     
print("Grade:", grade)   