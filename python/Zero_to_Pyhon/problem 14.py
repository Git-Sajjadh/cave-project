numbers_input=[]
numbers_input = input(f"Enter number with sapce: ")
number_input=numbers_input.split()
number_input=int(numbers_input())
print(f"num {number_input}")

even_num=[]
for i in len(numbers_input):
    if numbers_input%2==0:
        even_num=list(numbers_input)



print ("even", even_num)