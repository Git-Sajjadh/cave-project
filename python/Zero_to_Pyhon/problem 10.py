numbers=[]

for i in range(5):
    num=int(input(f"Enter Number {i+1}:"))
    numbers.append(num)

numbers.reverse()

print(f"Reverse list: {numbers}")