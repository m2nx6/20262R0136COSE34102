
# Python Basics 05: Loops

accuracies = [0.85, 0.91, 0.88, 0.94, 0.90]

# 1. Calculate average accuracy using a for loop
total = 0

for accuracy in accuracies:
    total += accuracy

average = total / len(accuracies)
print(f"Average accuracy: {average:.2%}")

# 2. Use enumerate to track experiment numbers
for index, accuracy in enumerate(accuracies, start=1):
    print(f"Experiment {index}: {accuracy:.2%}")

# 3. Count experiments above the threshold
threshold = 0.90
count = 0

for accuracy in accuracies:
    if accuracy >= threshold:
        count += 1

print("Experiments meeting threshold:", count)

# 4. Use while to simulate training epochs
epoch = 1
max_epochs = 5

while epoch <= max_epochs:
    print(f"Training epoch {epoch}/{max_epochs}")
    epoch += 1

# 5. Use break and continue
for accuracy in accuracies:
    if accuracy < 0.90:
        continue

    print(f"Qualified accuracy: {accuracy:.2%}")

    if accuracy >= 0.94:
        print("Target reached!")
        break
