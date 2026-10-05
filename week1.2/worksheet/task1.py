import sys
try:
    lut = ["Fail", "Pass", "Distinction"]
    grade=int(input("Please enter an integer grade in the range 0-100 "))
    result=grade
    if grade>100 or grade<0:
        sys.exit("Error: Grade must be an integer between 0 and 100")
    grade=grade-10
    grade=grade//30
    grade=max(grade, 0)
    grade=min(grade, 2)
    print(f"{result} is a {lut[grade]}")
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")