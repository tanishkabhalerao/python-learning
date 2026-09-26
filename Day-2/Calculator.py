Number_1 = int(input("enter first no."))
Number_2 = int(input("enter second no."))
operator = input("enter operator")

if operator =="*":
    print("output=", Number_1*Number_2)
elif operator == "/":
    print("output=",Number_1/Number_2)
elif operator == "+":
    print("output=",Number_1+Number_2)
else:
    print("output=",Number_1-Number_2)