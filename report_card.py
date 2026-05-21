print("REPORT CARD")

name = str(input("Enter the name: "))

cn = float(input("Enter the mark of CN: "))
ai = float(input("Enter the mark of AI: "))
dbdm = float(input("Enter the mark of DBDM: "))
daa = float(input("Enter the mark of DAA: "))
ps = float(input("Enter the mark of PS: "))

if (cn >= 50 and ai >= 50 and dbdm >= 50 and daa >= 50 and ps >= 50):
    
    print("Pass")
    
    total = cn + ai + dbdm + daa + ps
    average = total / 5

    print("The average is:", average)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "E"

    print("Grade:", grade)

else:
    print("Fail")
