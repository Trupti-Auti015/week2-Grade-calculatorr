#Students Grade Calculator  

name = input("enter student name: ")
mark = int(input("enter marks:"))

if mark >=90:
    grade = "A"
    Message = "Excellent work"
    
elif mark >=80:
    grade = "B"
    Message = "very good"

elif mark>=70:
    grade = "c"
    Message = "good job"
    
elif mark>=60:
    grade = "D"
    Message = "you Can improve"
    
else:
    grade = "f"
    Message = "Practice more"
   
print("\n----- Result -----") 
print("Name:", name)
print("Marks:", mark)
print("Grade:", grade)
print("Message:", Message)