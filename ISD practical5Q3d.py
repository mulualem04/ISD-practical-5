grade=float(input("Enter Score Grade: "))
if grade >= 90: # followed by indented block
    letterGrade = "A"
elif grade >= 80: # each elif are followed by indented block
    letterGrade = "B"
elif grade >= 70:
    letterGrade = "C"    
elif grade >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"     
