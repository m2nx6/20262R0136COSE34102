
# Python Basics 06: Functions

# Calculate average accuracy
def calculate_average(accuracies):
    if not accuracies:
        return 0.0
    return sum(accuracies) / len(accuracies)


# Find the highest accuracy
def find_best_accuracy(accuracies):
    if not accuracies:
        return None
    return max(accuracies)


# Count experiments meeting a threshold
def count_qualified(accuracies, threshold=0.90):
    count = 0

    for accuracy in accuracies:
        if accuracy >= threshold:
            count += 1

    return count


# Combine results into a dictionary
def analyze_results(accuracies):
    return {
        "average": calculate_average(accuracies),
        "best": find_best_accuracy(accuracies),
        "qualified": count_qualified(accuracies)
    }


# Example experiment results
accuracies = [0.85, 0.91, 0.88, 0.94, 0.90]

results = analyze_results(accuracies)

print(f"Average accuracy: {results['average']:.2%}")
print(f"Best accuracy: {results['best']:.2%}")
print(f"Qualified experiments: {results['qualified']}")

# Call the same function with different data
new_accuracies = [0.92, 0.95, 0.97]

print("New experiment analysis:")
print(analyze_results(new_accuracies))
