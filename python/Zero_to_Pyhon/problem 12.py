numbers = input("Enter numbers separated by space: ")
numbers = list(map(int, numbers.split()))
unique_numbers = list(set(numbers))
if len(unique_numbers) > 1:
    unique_numbers.sort()
    print("The 2nd largest number is:", unique_numbers[-2])
else:
    print("There is no 2nd largest number, all numbers are the same.")