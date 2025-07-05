first_num=int(input("Enter first number: "))
second_num=int(input("Enter second number: "))

if first_num>second_num:
    print(first_num,"is larger")
if first_num<second_num:
    print(second_num,"is larger")
elif first_num == second_num:
    print("Both numbers are equal")