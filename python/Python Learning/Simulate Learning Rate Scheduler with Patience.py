import random

learning_rate = 0.1
patience_limit = 3
max_epochs = 15
best_accuracy = 0
no_improvement = 0

for epoch in range(1, max_epochs + 1):
    acc = random.randint(70, 100)

    if acc > best_accuracy:
        best_accuracy = acc
        no_improvement = 0
        status = "✅ Improved"
    else:
        no_improvement += 1
        status = f"⚠️ No Improvement ({no_improvement})"

    print(f"Epoch {epoch} → Accuracy: {acc}% | LR: {learning_rate:.4f} | {status}")

    if no_improvement == patience_limit:
        learning_rate /= 2
        no_improvement = 0
        print(f"  🔻 Learning rate reduced to {learning_rate:.4f} due to no improvement\n")

print(f"\n🏁 Training complete. Best accuracy: {best_accuracy}% | Final LR: {learning_rate:.4f}")
