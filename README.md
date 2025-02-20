# NorthCarolina_CameroonChapter_AngusIssues
https://www.omdena.com/chapter-challenges/angus-issues-using-eda-and-forecasting-of-best-animal-science-practices

"North Carolina, USA Chapter", "Cameroon Chapter" - Angus Issues: Using EDA and Forecasting of Best Animal Science Practices

## **Overview**
This project is part of **Omdena’s North Carolina & Cameroon Local Chapter Challenge**.  
The goal is to **forecast cattle growth trends** using machine learning models and time-series forecasting techniques.  
This helps ranchers optimize livestock management practices and enhance resource planning.  

## **Key Features**
✔ **Predictive modeling** using **ARIMA, LSTM, SARIMA** for cattle growth forecasting  
✔ **Exploratory Data Analysis (EDA)** to identify key livestock growth trends  
✔ **Automated ETL pipeline** following **Object-Oriented Programming (OOP) principles** for modular data processing  
✔ **Flask API deployment** for real-time cattle growth prediction  
✔ **Version-controlled ML workflow** using **DVC, YAML, and CI/CD**  

---

## **📊 Data & Methodology**

### **1️⃣ Data Sources**
📌 Historical cattle weight records  
📌 Environmental factors (temperature, humidity, feed intake, etc.)  
📌 Health & breeding patterns  

### **2️⃣ Data Preprocessing**
🔹 Missing values handled using **KNN imputer & mean imputation**  
🔹 Feature selection using **Mutual Information & Recursive Feature Elimination (RFE)**  
🔹 Scaling applied using **StandardScaler & MinMaxScaler**  

### **3️⃣ Machine Learning Models**
✅ **ARIMA, SARIMA, and LSTM** for time-series forecasting  
✅ Feature engineering using **PCA** to improve model performance  
✅ **Hyperparameter tuning** using **GridSearchCV**  

### **4️⃣ Model Deployment**
🔹 **Flask API** for real-time predictions  
🔹 **DVC** for tracking datasets and model versions  
🔹 **Automated model retraining** using a **modular pipeline**  

---

## **⚙️ How to Run the Project**

### **1️⃣ Environment Setup**
Run the following commands in the terminal:

```bash
# Create a virtual environment
conda create -p venv python=3.8 -y  
conda activate venv/  
pip install -r requirements.txt  


## Workflows

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity 
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py

# How to run?
### STEPS:


```bash
conda create -p venv python=3.8 -y 
```

```bash
conda activate venv/
```


```bash
pip install -r requirements.txt
```

```bash
python app.py
```

```bash
Now open up your local host 0.0.0.0:8080
```
