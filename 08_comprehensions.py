
# Python Basics 08: List Comprehensions

experiments = [
    {"model": "MLP", "accuracy": 0.85},
    {"model": "CNN", "accuracy": 0.92},
    {"model": "ResNet", "accuracy": 0.96},
    {"model": "Transformer", "accuracy": 0.94},
    {"model": "SVM", "accuracy": 0.88}
]

# 1. Extract accuracy values
accuracies = [exp["accuracy"] for exp in experiments]
print("Accuracies:", accuracies)

# 2. Filter high-performing models
qualified = [
    exp for exp in experiments
    if exp["accuracy"] >= 0.90
]

print("\nQualified models:")
for exp in qualified:
    print(exp["model"])

# 3. Convert accuracy values to percentages
percentages = [acc * 100 for acc in accuracies]
print("\nPercentages:", percentages)

# 4. Create model summaries
summaries = [
    f"{exp['model']}: {exp['accuracy']:.1%}"
    for exp in experiments
]

print("\nSummaries:")
for summary in summaries:
    print(summary)

# 5. Dictionary comprehension
model_scores = {
    exp["model"]: exp["accuracy"]
    for exp in experiments
}

print("\nModel scores:", model_scores)
