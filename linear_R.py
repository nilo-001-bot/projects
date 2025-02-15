# Import necessary libraries
import numpy as np  # For numerical operations and array handling
import matplotlib.pyplot as plt  # For data visualization
from sklearn.linear_model import LinearRegression  # For linear regression model



# Create input features (time studied) and target variable (scores)
# Reshape to 2D array as required by scikit-learn
time_studied = np.array([20, 50, 32, 65, 23, 43, 10, 52, 23, 52, 95, 56]).reshape(-1, 1)
scores = np.array([56, 83, 47, 93, 47, 82, 45, 78, 55, 67, 57, 89]).reshape(-1, 1)




# Create and train the linear regression model
model = LinearRegression()
model.fit(time_studied, scores)  # Fit the model to our data



# Make a prediction for 56 hours of study
predicted_score = model.predict(np.array([56]).reshape(-1, 1))
print(f"Predicted score for 56 hours of study: {predicted_score[0][0]:.2f}")


# Visualize the data and regression line
plt.scatter(time_studied, scores, label='Actual Scores')  # Plot actual data points
x_values = np.linspace(0, 100, 100).reshape(-1, 1)  # Create x values for prediction
plt.plot(x_values, model.predict(x_values), 'r', label='Regression Line')  # Plot regression line

# Set plot limits and labels
plt.ylim(0, 100)
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Linear Regression: Study Time vs Test Score')
plt.legend()
plt.show()  # Display the plot
