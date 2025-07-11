true_labels =    [1, 0, 1, 1, 0, 0, 1]
predictions =    [1, 0, 0, 1, 0, 1, 1]


tp, tn, fp, fn = 0, 0, 0, 0

for true , predicted in zip(true_labels,predictions):
    if true == 1 and predicted == 1:
        tp += 1
    elif true == 0 and predicted == 0:
        tn += 1
    elif true == 0 and predicted == 1:
        fp += 1
    elif true == 1 and predicted == 0:
        fn += 1

print(f"True Positives: {tp} \nTrue Negatives: {tn} \nFalse Positives: {fp}\nFalse Negatives: {fn}")