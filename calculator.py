print("CALCULATOR")
a=float(input("enter the value of a:"))
b=float(input("enter the value of b:"))
print("the value of a:",a)
print("the value of b:",b)
print("enter your choice:")
print("+","-","*","/","%")
choice=input("enter the choice")
if(choice == "+"):
    c=a+b
    print("add of",a,"and",b,"is",c)
elif( choice == "-"):
    c=a-b
    print("sub of",a,"and",b,"is",c)
    
elif( choice == "*"):
    c=a*b
    print("mul of",a,"and",b,"is",c)   

elif( choice == "/"):
    c=a/b
    print("div of",a,"and",b,"is",c)   

elif( choice == "%"):
    c=a%b
    print("mod of",a,"and",b,"is",c)

else:
    print("Invalid choice")
                                                    
