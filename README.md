# Titanic Survival Prediction

A machine learning classification project that predicts whether a passenger survived the Titanic disaster based on passenger-related features such as age, gender, passenger class, fare, and family information. The project includes data preprocessing, exploratory data analysis, feature engineering, feature scaling, training multiple machine learning models, model evaluation, and deployment using Streamlit.

## 📁 Project Structure

**titanic-survival-prediction/**

- `app.py` - Streamlit application
- `classification.ipynb` - Jupyter Notebook for data analysis and model training
- `Logistic Regression.pkl` - Trained Logistic Regression model
- `scalar.pkl` - Saved StandardScaler
- `columns.pkl` - Saved feature/column information
- `.vscode/` - VS Code configuration

## 🔄 Project Workflow

**Data Collection → Data Preprocessing → Exploratory Data Analysis → Feature Engineering → Feature Scaling → Model Training → Model Evaluation → Model Saving → Streamlit Deployment → Survival Prediction**

## 🤖 Machine Learning Models

Five classification algorithms were trained and evaluated:

- **Logistic Regression** - A linear classification algorithm used for predicting passenger survival.
- **K-Nearest Neighbors (KNN)** - Classifies passengers based on the characteristics of their nearest neighbors.
- **Support Vector Machine (SVM)** - Finds an optimal decision boundary for classifying passengers into survival and non-survival classes.
- **Decision Tree Classifier** - Uses a tree-based structure and decision rules to classify passenger survival.
- **Gaussian Naive Bayes** - A probabilistic classification algorithm based on Bayes' theorem.

The trained models were evaluated using the test dataset, and the model used for the Streamlit prediction application was saved using Joblib.

## 🧹 Data Preprocessing

The dataset was prepared using:

- Missing-value checking and handling
- Duplicate-value checking
- Exploratory data analysis
- Categorical feature encoding
- Feature engineering
- Feature selection
- Train-test splitting
- Feature standardization using **StandardScaler**

## 📊 Model Evaluation

The trained models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

The performance of the five classification models was compared using the test dataset.

## 🚀 Deployment

The trained machine learning model was saved using **Joblib** along with the preprocessing objects:

- `Logistic Regression.pkl` - Saved Logistic Regression model
- `scalar.pkl` - Saved feature scaler
- `columns.pkl` - Saved model input feature information

These files can be loaded by the **Streamlit application (`app.py`)** to process passenger inputs and generate survival predictions.

## 🖥️ Application

The Streamlit application provides an interactive interface where users can enter passenger information and receive a predicted survival result.

The application processes the user input using the saved preprocessing objects and passes the processed features to the trained machine learning model.

## 🛠️ Tech Stack

**Python • Pandas • NumPy • Matplotlib • Seaborn • Scikit-learn • Logistic Regression • KNN • SVM • Decision Tree • Gaussian Naive Bayes • StandardScaler • Streamlit • Joblib • Jupyter Notebook**

## ✨ Key Features

- Titanic passenger survival prediction
- Multiple machine learning classification models
- Data preprocessing and cleaning
- Exploratory data analysis and visualization
- Feature engineering
- Feature scaling
- Model performance comparison
- Logistic Regression, KNN, SVM, Decision Tree, and Naive Bayes
- Saved trained machine learning models
- Saved preprocessing objects
- Streamlit-based prediction interface
- End-to-end machine learning workflow

## ⚠️ Disclaimer

This project is created for educational and demonstration purposes. The prediction is based on a machine learning model trained on historical Titanic passenger data.
