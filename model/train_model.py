import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
data = pd.read_csv(r"C:\Users\HP\Documents\Projects\Customer-Churn-Project\dataset\churn.csv")

# Select simple features
X = data[['tenure','MonthlyCharges']]
y = data['Churn'].map({'Yes':1,'No':0})

# Split data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train,y_train)

# Save model
pickle.dump(model,open("model.pkl","wb"))

print("Model trained and saved")