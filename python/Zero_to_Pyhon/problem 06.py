first_num=int(input("Enter first number: "))
second_num=int(input("Enter second number: "))
oprator=input("(+, -, *, /): ")

if oprator == "+":
    print("Result: ", first_num+second_num)
elif oprator == "-":
    print("Result: ", first_num-second_num)
elif oprator == "*":
    print("Result: ", first_num*second_num)
elif oprator == "/":
    print("Result: ", first_num/second_num)