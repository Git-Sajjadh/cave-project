numbers=[]
positive_count= 0
negative_count= 0

for i in range(5):
    add_numbers=int(input(f"Enter number {i+1} :"))
    
    if add_numbers>=0:
        positive_count +=1
    else: 
        negative_count +=1

    numbers.append(add_numbers)

print("positive_count: ", positive_count)
print("negative_count: ", negative_count)
