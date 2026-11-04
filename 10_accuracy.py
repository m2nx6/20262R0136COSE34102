
# Python Basics 10: Model Accuracy Evaluation

def calculate_accuracy(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("Input lengths must match.")

    if not y_true:
        raise ValueError("Input lists cannot be empty.")

    correct = 0

    for actual, predicted in zip(y_true, y_pred):
        if actual == predicted:
            correct += 1

    return correct / len(y_true)


def evaluate_model(model_name, y_true, y_pred):
    accuracy = calculate_accuracy(y_true, y_pred)

    return {
        "model": model_name,
        "accuracy": accuracy,
        "total_samples": len(y_true),
        "correct_predictions": sum(
            actual == predicted
            for actual, predicted in zip(y_true, y_pred)
        )
    }


# Ground truth labels
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]

# Predictions from two example models
mlp_predictions = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1]
cnn_predictions = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]

# Evaluate both models
mlp_result = evaluate_model("MLP", y_true, mlp_predictions)
cnn_result = evaluate_model("CNN", y_true, cnn_predictions)

for result in [mlp_result, cnn_result]:
    print(f"Model: {result['model']}")
    print(f"Accuracy: {result['accuracy']:.2%}")
    print(f"Correct: {result['correct_predictions']}")
    print(f"Total: {result['total_samples']}")
    print()

# Compare model performance
if mlp_result["accuracy"] > cnn_result["accuracy"]:
    print("MLP performs better.")
elif mlp_result["accuracy"] < cnn_result["accuracy"]:
    print("CNN performs better.")
else:
    print("Both models have equal accuracy.")
