# STRIDE: Type 2 Diabetes Risk Prediction System

STRIDE is a machine learning–based clinical decision support prototype that predicts Type 2 diabetes risk using structured clinical and demographic features. The system compares Logistic Regression and Random Forest models, analyzes feature importance, and deploys an interactive Streamlit application.

A key finding is the consistent dominance of HbA1c as the strongest predictor across both models.

---

# System Overview

The pipeline includes:

- Data preprocessing and feature engineering  
- Training Logistic Regression and Random Forest models  
- Model evaluation using accuracy, precision, recall, and F1 score  
- Feature interpretability using odds ratios and feature importance  
- Risk stratification based on predicted probabilities  
- Deployment via Streamlit web application  

---

# Models

## Logistic Regression
- Interpretable linear classifier  
- Outputs coefficients and odds ratios  
- Used for clinical interpretation of feature impact  

## Random Forest
- Ensemble-based nonlinear classifier  
- Captures feature interactions  
- Higher predictive performance  

---

# Key Findings

- HbA1c is the most influential predictor of Type 2 diabetes risk  
- Logistic Regression confirms HbA1c has the highest odds ratio  
- Random Forest assigns highest feature importance to HbA1c  
- Model agreement strengthens robustness of findings  
- Combined metabolic and physiological features improve prediction performance  

---

# Dataset

The dataset includes structured clinical variables:

- Age  
- Gender  
- BMI  
- Blood glucose level  
- HbA1c level  
- Hypertension status  

A previous attempt using the Pima Indians Diabetes Dataset was replaced due to missing HbA1c and limited clinical feature representation.

---

# Feature Interpretation

Logistic Regression coefficients were transformed into odds ratios to quantify feature influence on diabetes risk.

Key interpretation:

- HbA1c shows the strongest positive association with diabetes risk  
- BMI and hypertension show moderate influence  
- Age and gender contribute lower predictive power  

---

# Risk Stratification

Model outputs are converted into clinical risk categories:

- Low Risk  
- Moderate Risk  
- High Risk  
- Very High Risk  

Thresholds are derived from predicted probability distributions.

---

# Streamlit Application
Live Demo: https://edificient.streamlit.app/
The web application enables:

- Patient input interface for clinical variables  
- Real-time risk prediction  
- Model comparison (Logistic Regression vs Random Forest)  
- Risk category classification  
- Clinical interpretation of predictions  

---

# Installation

## 1. Clone repository
```
git clone https://github.com/yourusername/stride.git  
cd stride  
```
## 2. Create virtual environment (recommended)
```
python -m venv venv  
```
Mac/Linux  
```
source venv/bin/activate  
```
Windows  
```
venv\Scripts\activate  
```
## 3. Install dependencies
```
pip install -r requirements.txt  
```

# Usage

## Run Streamlit app
```
streamlit run app.py  

Then open:

http://localhost:8501  
```

# Limitations

- Dataset does not include full clinical, genetic, or lifestyle variables  
- No external validation on real hospital data  
- Risk thresholds are not clinically calibrated  
- Model may not generalize beyond training distribution  
- Intended for educational and research purposes only  


# Future Work

- Integration of real-world clinical datasets  
- Probability calibration for clinical reliability  
- Addition of lifestyle and longitudinal health features  
- External validation using hospital datasets  
- Deployment as a clinical decision support prototype  
- Expansion to multi-disease risk prediction systems  


# DISCLAIMER

This project is for educational and research purposes only.

It is not a medical device and should not be used for clinical diagnosis, treatment decisions, or patient care.
```
