# 🚀 Network Anomaly Detection using Machine Learning

## 📌 Project Overview:
- In today’s cybersecurity landscape, detecting anomalous network behavior is critical to prevent attacks such as DDoS, intrusions, and unauthorized access. 
- Traditional rule based systems fail to detect evolving threats, making machine learning a powerful alternative.
- This project builds an end to end anomaly detection system using supervised and unsupervised ML techniques to identify suspicious network activity in real time.

## 🎯 Objective
- Detect anomalous network connections from normal traffic
- Build a robust classification system to distinguish normal vs anomalous network traffic
- Improve detection accuracy while minimizing false negatives
- Enable real time prediction through API deployment

## 📂 Dataset Description
- Basic Features: Duration, Protocol Type, Service, Flag, Bytes transferred
- Content Features: Login attempts, root access, file & shell activity
- Time-Based Features: Connection count, error rates
- Host-Based Features: Destination host behavior patterns

## 🔍 Exploratory Data Analysis (EDA)
- Analyzed distribution of normal vs attack traffic
- Identified strong correlations between traffic features
- Detected outliers indicating anomalous behavior
- Evaluated protocol & service-level attack patterns
- Validated hypotheses using statistical testing

## 📊 Hypothesis Testing

- Statistical hypothesis testing to validate differences between normal and anomalous traffic
- Mann–Whitney U Test for continuous features (non-normal, skewed data)
- Chi-Square Test for categorical relationships

## 🤖 Machine Learning Approach
- Models Used : Random Forest, Isolation Forest
- Evaluation Metrics : Accuracy, Precision, Recall, F1 Score, ROC-AUC

## 📊 Key Results
- Accuracy: ~99%
- Recall (Anomaly Detection): ~99%
- ROC-AUC: ~0.99

## 🚀 Deployment (Flask API)
- Accepts network traffic data (JSON)
- Applies preprocessing
- Returns anomaly prediction
- Sample API Flow: Input → Preprocessing → Model → Prediction (Normal / Anomaly)

## 💡 Business Impact
- Enables real time threat detection
- Reduces dependency on rule based systems
- Scales across large enterprise networks
- Improves operational security & compliance 

## 👨🏻‍💻 About Me
Mohit Suthar — Data Scientist & Audit Analytics Professional with a knack for spotting anomalies and asking “what’s going wrong here?”
10+ years of experience across enterprise analytics, automation, and large scale data systems.
🔗 Connect with Me
- ([LinkedIn](https://www.linkedin.com/in/mohitsuthar22/))
- ([GitHub](https://github.com/MrRobotV22))