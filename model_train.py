import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Load the combined dataset
data = pd.read_csv('combined_stock_sentiment_data.csv')

# Display the first few rows of the dataset
print(data.head())

# Prepare features (X) and target (y)
X = data[['Open', 'High', 'Low', 'Volume', 'sentiment']].fillna(0)
y = data['Close']  # Target variable

# Feature scaling (Standardizing)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Cross-validation to validate model performance
cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
print(f"Cross-Validation R^2 Scores: {cv_scores}")
print(f"Mean Cross-Validation R^2: {cv_scores.mean()}")

# Make predictions
y_pred = model.predict(X_test)

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print performance
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Feature Importance
importances = model.feature_importances_
feature_names = ['Open', 'High', 'Low', 'Volume', 'Sentiment']

# Display feature importances
feature_importances = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_importances.sort_values(by='Importance', ascending=False, inplace=True)
print("\nFeature Importances:\n", feature_importances)
