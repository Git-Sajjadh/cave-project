numbers=[]

for i in range(5):
    num=int(input(f"Enter Number {i+1} :"))
    numbers.append(num)

max_num= max(numbers)
print(f"The largest number is: {max_num}")