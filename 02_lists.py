
# Python Basics 02: Lists and Data Analysis

# Accuracy results from five experiments
accuracies = [0.85, 0.91, 0.88, 0.94, 0.90]

# Access list elements
print("First accuracy:", accuracies[0])
print("Last accuracy:", accuracies[-1])

# Basic statistics
best_accuracy = max(accuracies)
worst_accuracy = min(accuracies)
average_accuracy = sum(accuracies) / len(accuracies)

print("Best accuracy:", best_accuracy)
print("Worst accuracy:", worst_accuracy)
print("Average accuracy:", average_accuracy)

# Add a new experiment result
accuracies.append(0.96)

print("Updated accuracies:", accuracies)
print("Number of experiments:", len(accuracies))
