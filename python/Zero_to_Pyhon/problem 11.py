
user_input=input("Enter a word or sentence:")
vowel_count=0
vowels="aeiouAEIOU"

for i in user_input:
    if i in vowels:
        vowel_count +=1

print(f"Nmbers of vowels: {vowel_count}")