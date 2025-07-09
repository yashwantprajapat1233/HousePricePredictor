# 🏠 House Price Predictor – California Housing Data

A Machine Learning web app built using **Streamlit** and **Random Forest Regressor** to predict the **median house value** based on housing and geographic features from the California housing dataset.

---

## 📊 Project Overview

This project explores California housing data, builds multiple regression models, and deploys an interactive web app for users to predict house prices based on:

- Location (latitude, longitude)
- Housing characteristics (rooms, age, income, population)
- Proximity to the ocean

---

## 🔍 Key Features

- ✅ Interactive Streamlit UI with sliders and dropdowns
- ✅ Real-time price prediction using trained **Random Forest** model
- ✅ Supports one-hot encoded `ocean_proximity`
- ✅ Model comparison (Linear Regression, Decision Tree, XGBoost, Random Forest)
- ✅ Clean and responsive layout

---

## 🧠 ML Techniques Used

- Data Cleaning & Handling Missing Values
- Feature Engineering & One-Hot Encoding
- Model Training:  
  - Linear Regression  
  - Decision Tree  
  - Random Forest (Best Performance)  
  - XGBoost
- Model Evaluation: R² Score & MSE
- Model Persistence using `joblib`

---

## 📈 Model Performance

| Model              | R² Score | MSE               |
|--------------------|----------|-------------------|
| Linear Regression  | 0.6257   | 4.90 × 10⁹        |
| Decision Tree      | 0.6281   | 4.87 × 10⁹        |
| Random Forest      | 0.8166   | 2.40 × 10⁹ ✅      |
| XGBoost            | 0.8037   | 2.57 × 10⁹        |

✅ **Random Forest** selected as final model.

---

## 🚀 How to Run

### 🧩 Prerequisites


pip install -r requirements.txt



▶️ Start the Streamlit app

  streamlit run streamlit_app.py

  
⚠️ Note on Model File
Due to GitHub’s 100MB file size limit, the trained model file:

plaintext
Copy
Edit
random_forest_model.pkl
is not uploaded to the repository. To generate it manually:

Open the housing_project_notebook.ipynb

Train the model using the Random Forest cell

Save the model:

python
Copy
Edit
import joblib
joblib.dump(model, 'random_forest_model.pkl')
Once saved, you can run the Streamlit app as normal.

🗂️ Project Structure

HousePricePredictor/
│
├── housing.csv                    # Dataset
├── model_features.pkl             # Saved feature columns
├── random_forest_model.pkl        # Trained model (local only, ignored in Git)
├── streamlit_app.py               # Streamlit web app
├── housing_project_notebook.ipynb # Notebook with full EDA + training
├── .gitignore
├── requirements.txt
└── README.md



🙋‍♂️ Author
Yashwant Prajapat
📫 prajapatiyashwant1233@gmail.com
🔗 LinkedIn
📁 GitHub Portfolio

❤️ Acknowledgements
Dataset: California Housing — Kaggle

Inspired by real estate price prediction and ML deployment learning paths.
