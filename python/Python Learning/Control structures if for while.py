scores = [0.92, 0.85, -0.1, 0.5, 1.1, 0.75, 0.65, 0.99, -0.5, 0.45, 0.88]

valid_values = []
invalid_values = []

high_count = 0
medium_count = 0
low_count = 0

for score in scores:
    if 0 <= score <= 1:
        valid_values.append(score)

        if score >= 0.9:
            print(f"{score} → High")
            high_count += 1
        elif score >= 0.7:
            print(f"{score} → Medium")
            medium_count += 1
        else:
            print(f"{score} → Low")
            low_count += 1
    else:
        invalid_values.append(score)

print("\n=== Summary ===")
print(f"Valid: {valid_values}")
print(f"Invalid: {invalid_values}")
print(f"High: {high_count}, Medium: {medium_count}, Low: {low_count}")
