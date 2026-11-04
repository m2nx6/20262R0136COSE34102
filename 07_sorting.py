
# Python Basics 07: Sorting Experiment Results

experiments = [
    {"model": "MLP", "accuracy": 0.85},
    {"model": "CNN", "accuracy": 0.92},
    {"model": "ResNet", "accuracy": 0.96},
    {"model": "Transformer", "accuracy": 0.94},
    {"model": "SVM", "accuracy": 0.88}
]

# 1. Sort experiments by accuracy (descending)
ranked = sorted(
    experiments,
    key=lambda exp: exp["accuracy"],
    reverse=True
)

print("Model Ranking:")
for rank, experiment in enumerate(ranked, start=1):
    print(
        f"{rank}. {experiment['model']}: "
        f"{experiment['accuracy']:.2%}"
    )

# 2. Select the top 3 models
top_3 = ranked[:3]

print("\nTop 3 Models:")
for experiment in top_3:
    print(experiment["model"])

# 3. Sort by model name (alphabetical order)
alphabetical = sorted(
    experiments,
    key=lambda exp: exp["model"]
)

print("\nAlphabetical Order:")
for experiment in alphabetical:
    print(experiment["model"])

# 4. Check whether the original list changed
print("\nOriginal first model:", experiments[0]["model"])
