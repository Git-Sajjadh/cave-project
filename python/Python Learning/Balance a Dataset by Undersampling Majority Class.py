import random

labels = ['cat', 'dog', 'dog', 'cat', 'dog', 'cat', 'cat', 'dog', 'dog', 'dog']
cat=[]
dog=[]
for animal in labels:
    if animal == "cat":
        cat.append("cat")
    else:
        dog.append("dog")

min_count = min(len(cat), len(dog))
random.shuffle(cat)
random.shuffle(dog)

balanced = cat[:min_count] + dog[:min_count]
random.shuffle(balanced)

print("Balanced dataset:", balanced)