<h1 align="center">📉 Telecom Customer Churn Prediction</h1>
<p align="center">
  <strong>Leveraging machine learning to identify at-risk customers and enhance retention strategies</strong>
</p>



---

## 🌐 Dataset
- **Source**: Kaggle ([Dataset Link](https://www.kaggle.com/blastchar/telco-customer))  
- **Description**: Contains customer demographics, service details, and churn labels  
- **Preprocessing**: Handled missing values, encoded categorical features, and normalized numerical data  

---

## 📝 Project Overview
This project builds a predictive model to **detect customer churn** in the telecom sector. By utilizing **data preprocessing, imbalance handling, and robust classifiers**, it provides actionable insights to reduce churn and improve customer retention.

---

##  Key Features

### 🔹 1. Data Preprocessing
- Addressed missing values and inconsistent entries  
- Converted categorical features using **one-hot encoding**  
- Scaled numerical variables to optimize model performance  

### 🔹 2. Imbalanced Data Handling
- Applied **SMOTEENN (Synthetic Minority Over-sampling and Edited Nearest Neighbors)** to balance the dataset  
- Improved recall for churned customers while maintaining overall model stability  

### 🔹 3. Model Training & Evaluation
- Implemented **Decision Tree** and **Random Forest** classifiers  
- Assessed model performance using:
  - **Precision, Recall, F1-Score, and Confusion Matrix**
- **Achieved 92.36% accuracy** with the Random Forest model  

### 🔹 4. Model Deployment
- Saved the trained model as `model.sav`  
- Ready for **API integration** to enable real-time churn prediction  

---

## 🛠️ Technologies Used

| Category  | Tools & Libraries |
|-----------|------------------|
| **Programming** | Python |
| **Libraries** | `pandas`, `scikit-learn`, `imbalanced-learn`, `matplotlib` |
| **Techniques** | SMOTEENN, Decision Tree, Random Forest, Data Preprocessing |

---

## 📊 Model Performance
| Metric       | Decision Tree | Random Forest |
|--------------|--------------|--------------|
| **Accuracy** | 82.8% | 92.36% |
| **Precision** | Moderate | High |
| **Recall** | Low | High |
| **F1-Score** | Moderate | High |

- **Random Forest** significantly improved recall for churned customers, making it the preferred model.  

---

## 💡 Business Impact
✅ **Improved Churn Prediction** – More accurate detection of at-risk customers  
✅ **Data-Driven Decision Making** – Helps telecom providers implement proactive retention strategies  
✅ **Revenue Growth** – Reduces churn-related revenue losses  

---

## 🔗 Future Enhancements

SHAP-based explainability

Automated retraining schedule

Email/SMS alert integration

![Project Banner](Customer_chur_banner.png)
---

## 🤝 Contributing
Contributions are welcome! Feel free to **fork, improve, and submit a pull request**.  

For any questions, feel free to connect! 🚀  
