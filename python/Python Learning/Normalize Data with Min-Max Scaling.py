raw_values = [50, 80, 100, 65, 40]

min_value = min(raw_values)
max_value = max(raw_values)

normalized = []

for i in raw_values:
    if max_value != min_value:
        normalization = (i - min_value) / (max_value - min_value)
    else:
        normalization = 0  # Edge case: all values same

    normalized.append(normalization)
    print(f"Original: {i} → Normalized: {normalization:.2f}")

print("\nAll Normalized Values:", normalized)
