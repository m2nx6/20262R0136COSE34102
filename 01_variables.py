
# Python Basics 01: Variables and Data Types

model_name = "ResNet"
epochs = 10
learning_rate = 0.001
accuracy = 0.95
is_trained = True

print("Model:", model_name)
print("Epochs:", epochs)
print("Learning rate:", learning_rate)
print("Accuracy:", accuracy)
print("Training completed:", is_trained)

print("Type of accuracy:", type(accuracy))

summary = f"{model_name} achieved {accuracy * 100:.1f}% accuracy."
print(summary)
