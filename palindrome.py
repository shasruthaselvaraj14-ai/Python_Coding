n=str(input("enter the name:"))
print("the name is:",n)
rev = n[::-1]
if n == rev:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
