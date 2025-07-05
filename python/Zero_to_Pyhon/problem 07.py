Numbers=[]

for i in range(5):
    Num=int(input(f"Enter number {i+1} :"))
    Numbers.append(Num)

print("Number:", Numbers)
print("Sum:", sum(Numbers))