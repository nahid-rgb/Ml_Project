# Student Performance Predictor

A end-to-end Machine Learning web application that predicts a student's **Mathematics score** based on their background information such as gender, ethnicity, parental education, lunch type, and test preparation course.

🌐 **Live Demo:** [https://student-performance-predictor-nc5k.onrender.com](https://student-performance-predictor-nc5k.onrender.com)

---

## Problem Statement

Understand how a student's **Mathematics score** is affected by their background information.

---

### Input Features

These are the variables we know about the student:

| Feature | Type | Example Values |
|---|---|---|
| Gender | Categorical | male, female |
| Race / Ethnicity | Categorical | group A, group B, group C, group D, group E |
| Parental Level of Education | Categorical | bachelor's degree, master's degree, associate's degree, high school, some college, some high school |
| Lunch Type | Categorical | standard, free/reduced |
| Test Preparation Course | Categorical | completed, none |
| Reading Score | Numerical | 0 – 100 |
| Writing Score | Numerical | 0 – 100 |

---

### Output Feature

The variable we want to predict:

| Feature | Type | Range |
|---|---|---|
| Math Score | Numerical | 0 – 100 |

---

### Goal

Given a student's background and their reading and writing scores, **predict their Mathematics exam score** using machine learning.

---

## 📊 Dataset

- **Source:** [Kaggle — Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Rows:** 1000 students
- **Columns:** 8 features

---

## Project Structure

```
Ml_Project/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py        # reads and splits raw data
│   │   ├── data_transformation.py   # cleans and encodes features
│   │   └── model_trainer.py         # trains and selects best model
│   │
│   ├── pipeline/
│   │   └── predict_pipeline.py      # loads model and makes predictions
│   │
│   ├── exception.py                 # custom exception handler
│   ├── logger.py                    # logging configuration
│   └── utils.py                     # save/load object, evaluate models
│
├── artifacts/
│   ├── model.pkl                    # best trained model
│   ├── preprocessor.pkl             # fitted data transformer
│   ├── data.csv                     # original raw data
│   ├── train.csv                    # training split (80%)
│   └── test.csv                     # test split (20%)
│
├── templates/
│   ├── index.html                   # welcome page
│   └── home.html                    # prediction form and result
│
├── notebook/
│   ├── 1.eda_student_performance.ipynb   # exploratory data analysis
│   └── 2.model_training.ipynb            # model experimentation
│
├── application.py                   # Flask app entry point
├── Procfile                         # Render deployment config
├── requirements.txt                 # project dependencies
├── setup.py                         # project packaging
└── README.md
```

---

## ML Pipeline

```
Raw Data (CSV)
      ↓
Data Ingestion
      ↓ reads CSV, splits into train (80%) and test (20%)
Data Transformation
      ↓ handles missing values, encodes categories, scales numbers
Model Training
      ↓ trains 7 models, tunes hyperparameters, selects best
Best Model Saved (model.pkl)
      ↓
Prediction Pipeline
      ↓ loads model + preprocessor, transforms input, predicts
Flask Web App
      ↓
Live on Render
```

---

## Models Trained

| Model | Description |
|---|---|
| Linear Regression | Baseline model |
| Ridge | Linear with L2 regularization |
| Lasso | Linear with L1 regularization |
| Decision Tree | Tree-based model |
| Random Forest | Ensemble of decision trees |
| Gradient Boosting | Sequential boosting |
| XGBoost | Extreme gradient boosting |
| CatBoost | Handles categorical features natively |
| AdaBoost | Adaptive boosting |

Best model selected automatically based on **R² score** on test data.

---

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.11 |
| ML Libraries | scikit-learn, XGBoost, CatBoost |
| Data | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Web Framework | Flask |
| Deployment | Render |
| Version Control | Git, GitHub |

---

## ▶️ How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/nahid-rgb/Ml_Project.git
cd Ml_Project
```

**2. Create virtual environment**
```bash
conda create -p venv python==3.11 -y
conda activate venv/
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the app**
```bash
python application.py
```

**5. Open in browser**
```
http://localhost:5000
```

---

## 🌐 Deployment

Deployed on **Render** using Gunicorn as the production server.

```
Procfile → web: gunicorn application:app
```

Every push to the `main` branch automatically redeploys the app.

---
