import random

accuracy_required = 90
training_runs = 5

for run in range(1, training_runs + 1):
    accuracy = 50
    epoch = 0

    print(f"\n🚀 Training Run {run}")

    while accuracy < accuracy_required:
        improvement = random.randint(1, 10)
        accuracy += improvement
        epoch += 1
        print(f"  Epoch {epoch} → Accuracy: {accuracy}%")

    print(f"✅ Run {run} reached goal in {epoch} epochs with final accuracy: {accuracy}%")
