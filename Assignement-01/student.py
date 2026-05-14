Student_name: str = input("Enter Your Student Name")
Student_roll_number: int = input("Enter Your Student Roll Number ")

Subject_English_Marks: int = int(input("Enter Your Marks Of English"))
Subjec_Computer_Marks: int = int(input("Enter Your Marks Of Computer"))
Subjec_Physics_Marks: int = int(input("Enter Your Marks Of Physics"))
Subjec_Math_Marks: int = int(input("Enter Your Marks Of Math"))
Subjec_Urdu_Marks: int = int(input("Enter Your Marks Of Urdu"))

Total_Marks: int = Subject_English_Marks + Subjec_Computer_Marks + Subjec_Physics_Marks +Subjec_Math_Marks + Subjec_Urdu_Marks
print("Total Marks" , Total_Marks)
Percentage: float = (Total_Marks/500)*100

print("\n----- STUDENT RESULT -----")

print("Student Name:", Student_name)
print("Student Roll Number:", Student_roll_number)

print(f"Percentage: {Percentage:.5f}%")

if Percentage >= 80:
    print("Result: Pass")
    print("Grade: A+")
elif Percentage >= 70:
    print("Result: Pass")
    print("Grade: A")
elif Percentage >= 60:
    print("Result: Pass")
    print("Grade: B")
elif Percentage >= 50:
    print("Result: pass")
    print("Grade: C")
elif Percentage >= 40:
    print("Result: Pass")
    print("Grade: D")
else:
    print("Result: Fail")
