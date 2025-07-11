true_labels = ['cat', 'dog', 'cat', 'dog', 'cat', 'bird']
predicted_labels = ['cat', 'cat', 'cat', 'dog', 'bird', 'bird']

labels = list(zip(true_labels, predicted_labels))

total_correct = 0
total_samples = len(labels)

# Class-wise counters
class_totals = {'cat': 0, 'dog': 0, 'bird': 0}
class_correct = {'cat': 0, 'dog': 0, 'bird': 0}

for true, pred in labels:
    class_totals[true] += 1
    if true == pred:
        total_correct += 1
        class_correct[true] += 1

# Print accuracy
accuracy = (total_correct / total_samples) * 100
print(f"Overall Accuracy: {accuracy:.2f}%")

# Print class-wise breakdown
print("\nClass Breakdown:")
for label in class_totals:
    total = class_totals[label]
    correct = class_correct[label]
    print(f"{label} - Total: {total}, Correct: {correct}")
