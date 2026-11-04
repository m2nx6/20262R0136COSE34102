
# Python Basics 09: Exception Handling

def calculate_average(accuracies):
    if not accuracies:
        raise ValueError("Accuracy list cannot be empty.")

    for accuracy in accuracies:
        if not isinstance(accuracy, (int, float)):
            raise TypeError("Accuracy must be numeric.")

        if not 0 <= accuracy <= 1:
            raise ValueError("Accuracy must be between 0 and 1.")

    return sum(accuracies) / len(accuracies)


# 1. Valid experiment results
try:
    results = [0.85, 0.92, 0.96]
    average = calculate_average(results)
except (ValueError, TypeError) as error:
    print("Error:", error)
else:
    print(f"Average accuracy: {average:.2%}")
finally:
    print("First analysis completed.")


# 2. Empty data
try:
    calculate_average([])
except ValueError as error:
    print("Empty data error:", error)


# 3. Invalid accuracy value
try:
    calculate_average([0.85, 1.20, 0.90])
except ValueError as error:
    print("Invalid value error:", error)


# 4. Incorrect data type
try:
    calculate_average([0.85, "0.92", 0.90])
except TypeError as error:
    print("Type error:", error)
