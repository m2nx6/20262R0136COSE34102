
# Python Basics 03: Dictionaries

# Store machine learning experiment information
experiment = {
    "model": "ResNet",
    "accuracy": 0.95,
    "epochs": 10,
    "learning_rate": 0.001
}

# Access values using keys
print("Model:", experiment["model"])
print("Accuracy:", experiment["accuracy"])

# Add a new key-value pair
experiment["optimizer"] = "Adam"

# Update an existing value
experiment["accuracy"] = 0.96

# Iterate through the dictionary
for key, value in experiment.items():
    print(f"{key}: {value}")

# Store multiple experiments
experiments = {
    "exp_001": {"model": "MLP", "accuracy": 0.85},
    "exp_002": {"model": "CNN", "accuracy": 0.91},
    "exp_003": {"model": "ResNet", "accuracy": 0.96}
}

# Find the best experiment
best_experiment = max(
    experiments,
    key=lambda name: experiments[name]["accuracy"]
)

print("Best experiment:", best_experiment)
print("Best model:", experiments[best_experiment]["model"])
