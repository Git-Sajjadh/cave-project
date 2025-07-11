import random

epochs= 0
max_epochs = 20
best_accuracy = 0
no_improvement_count=0



while epochs<max_epochs:
    epochs += 1
    accuracy_improvement=random.randint(70,100)

    print(f"Epoch {epochs} → Accuracy: {accuracy_improvement}%")
    
    if accuracy_improvement>best_accuracy:
        best_accuracy=accuracy_improvement
        no_improvement_count=0
        print("  ✅ Accuracy improved!")
    else:
        no_improvement_count += 1
        print(f"  ⚠️ No improvement for {no_improvement_count} epoch(s)")
    if no_improvement_count==5:
            print("\n🛑 Early stopping triggered.")
            break

print(f"\nTraining stopped after {epochs} epochs. Best accuracy: {best_accuracy}%")