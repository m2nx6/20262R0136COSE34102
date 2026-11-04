
# Python Basics 04: Conditional Statements

# Machine learning experiment results
experiments = [
    {"model": "MLP", "accuracy": 0.85},
    {"model": "CNN", "accuracy": 0.92},
    {"model": "ResNet", "accuracy": 0.97},
    {"model": "Transformer", "accuracy": 0.89}
]

# Evaluate each model based on accuracy
for experiment in experiments:
    model = experiment["model"]
    accuracy = experiment["accuracy"]

    if accuracy >= 0.95:
        grade = "Excellent"
    elif accuracy >= 0.90:
        grade = "Good"
    elif accuracy >= 0.80:
        grade = "Average"
    else:
        grade = "Needs Improvement"

    print(f"{model}: {accuracy:.1%} - {grade}")

# Check whether a model meets the deployment threshold
deployment_threshold = 0.90

for experiment in experiments:
    if experiment["accuracy"] >= deployment_threshold:
        print(f"{experiment['model']} meets the threshold.")
    else:
        print(f"{experiment['model']} is below the threshold.")
