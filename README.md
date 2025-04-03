# 🏥 Liver Disease Prediction Using Machine Learning

## 📝 Objective
This project aims to predict liver disease in patients based on medical data using machine learning models. The dataset, sourced from Kaggle, contains various clinical attributes that help assess liver health conditions.

## 📂 Dataset
The dataset includes the following features:
- 👤 **Age** - Patient's age
- ⚧️ **Gender** - Male/Female
- 🩸 **Total Bilirubin** - Bilirubin levels in the blood
- 🩺 **Direct Bilirubin** - Direct form of bilirubin
- 🏥 **Alkaline Phosphatase (ALP)** - An enzyme related to liver and bone disorders
- 🩸 **Alanine Aminotransferase (ALT)** - An enzyme linked to liver function
- 🩸 **Aspartate Aminotransferase (AST)** - Another enzyme associated with liver health
- 🩹 **Total Proteins** - Protein levels in the blood
- 🥚 **Albumin** - A protein produced by the liver
- 🩸 **Albumin & Globulin Ratio (A/G Ratio)** - Ratio of liver-related proteins
- ✅ **Target Variable** - 1 (Liver Disease) / 0 (No Liver Disease)

## 🚀 Steps Involved
1️⃣ **Data Collection & Preprocessing:**
   - Load and explore the dataset
   - Handle missing values and outliers
   - Encode categorical variables (e.g., gender)
   - Normalize numerical features for better model performance

2️⃣ **Data Splitting:**
   - Divide the dataset into training and testing sets
   - Ensure class balance for better predictions

3️⃣ **Model Building & Training:**
   - Train multiple machine learning models (Logistic Regression, Random Forest, Decision Tree, etc.)
   - Compare performance metrics such as accuracy, precision, recall, and F1-score

4️⃣ **Model Selection & Evaluation:**
   - Choose the best-performing model based on results
   - Save the trained model as `.pkl` for future use

5️⃣ **Manual Testing:**
   - Load the saved model
   - Preprocess and make predictions on new patient data

6️⃣ **API Integration (Flask Web App):**
   - Build a simple web interface using Flask
   - Allow users to enter medical details and get liver disease predictions

## 🛠️ Technologies Used
- 🐍 **Python**
- 🤖 **Scikit-learn**
- 🔢 **Pandas & NumPy**
- 📊 **Matplotlib & Seaborn** (for visualization)
- 🌐 **Flask (for web app integration)**
- 🏗️ **Machine Learning Algorithms**


