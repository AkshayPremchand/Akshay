# Addition of two numbers
n1=int(input("enter a number1: \n"))
n2=int(input("enter a number2: \n"))
print(n1+n2)

# Number is even or odd
n=int(input("Enter a number: \n"))
if (n%2):
    print("odd")
else:
    print("even")

# Numbers up to n from 0
n=int(input("enter a number: \n"))
for i in range(n+1):
    print(i, end=" ")

# Numbers between n1 and n2
n1=int(input("enter a Number1: \n"))
n2=int(input("enter a Number2: \n"))
for i in range(n1, n2 + 1):
    print(i, end=" ")

# x in between n1 and n2
n1=int(input("enter a number1: \n"))
n2=int(input("enter a number2: \n"))
x=int(input("enter x: \n"))
for i in range(n1,n2+1):
    if i==x:
        print("yes")
        break
else:
    print("No, number is not in the range")

# even number between n1 and n2
n= int(input("enter a number \n"))
for i in range(0, n+1, 2):
    print(i, end=" ")

# even numbers between n1 and n2
n1=int(input("enter a number1: \n"))
n2=int(input("enter a number: \n"))
for i in range(n1, n2+1, 2):
    print(i, end=" ")

# odd numbers up to n
n= int(input("enter a number \n"))
for i in range(1, n+1, 2):
    print(i, end=" ")

# odd numbers between n1 and n2
n1=int(input("enter a number1: \n"))
n2=int(input("enter a number2: \n"))
for i in range(n1, n2+2):
    if i % 2!=0:
        print(i, end=" ")

# multiplication tabl up to 10
n=int(input("enter a table: \n"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")

#Operation
n1=int(input("enter a number1: \n"))
n2=int(input("enter a number2: \n"))
operator = input("enter operator(+,-,*,%): \n")
match operator:
    case"+":print(n1+n2)
    case"-":print(n1-n2)
    case"*":print(n1*n2)
    case"%":print(n1%n2)
    case default: print("invalid operator")