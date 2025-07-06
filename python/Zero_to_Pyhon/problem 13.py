input_num= []
input_num=input(f"Enter Number: ")

input_num=list(map(int,input_num.split()))
unique_num= list(set(input_num))

"""if len(unique_num)>1:
    unique_num.sort()
    print(f"The smallest unique number is: {unique_num[0]}")
else:
    print(f"No unique number found")"""

unique_once=[num for num in input_num if input_num.count(num) == 1]

if unique_once:
    print(f"The smallest unique number is: {min(unique_once)}")
else:
    print("No unique number found")