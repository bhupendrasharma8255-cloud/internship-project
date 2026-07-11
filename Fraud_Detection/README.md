# 💳 Fraud Detection System using K-Means Clustering

A Machine Learning web application that classifies financial transactions into **Genuine** or **Fraudulent** using the **K-Means Clustering** algorithm.

The project is developed using **Python**, **Flask**, **Scikit-learn**, **HTML**, and **CSS**. It provides a simple and interactive web interface where users can enter transaction details and receive an instant prediction.

---

## 🚀 Features

- Detects suspicious financial transactions
- Uses **K-Means Clustering (Unsupervised Learning)**
- Data preprocessing using **StandardScaler**
- Modern and responsive Flask web interface
- Predicts transaction cluster in real time
- Saves trained model using **Pickle**
- Clean and beginner-friendly project structure

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML5
- CSS3
- Pickle

---

## 📂 Project Structure

```text
Fraud_Detection/
│
├── Dataset/
│   └── fraud_detection.csv
│
├── model/
│   ├── kmeans_model.pkl
│   └── scaler.pkl
│
├── Notebook/
│   └── model_training.ipynb
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
└── requirment.txt
```

## 🏗️ Project Architecture Diagram
---



---

## 📊 Dataset

This project uses a **synthetic fraud detection dataset** created for educational purposes.

### Dataset Summary

| Item | Value |
|------|-------|
| Total Transactions | 50,000 |
| Genuine Transactions | 40,000 |
| Fraud Transactions | 10,000 |
| Fraud Ratio | 20% |

### Dataset Features

| Feature | Description |
|----------|-------------|
| Amount | Transaction amount |
| Hour | Transaction hour (0–23) |
| Distance_km | Distance from customer's usual location |
| Device_Score | Device trust score |
| Daily_Transactions | Number of daily transactions |
| Failed_Logins | Failed login attempts |
| International | Domestic or international transaction |
| Weekend | Weekend transaction indicator |
| Account_Age_Months | Customer account age |
| Fraud | Actual transaction label |

---

## 🤖 Machine Learning Workflow

1. Load Dataset
2. Data Preprocessing
3. Feature Selection
4. Feature Scaling using StandardScaler
5. Find Optimal K using Elbow Method
6. Validate using Silhouette Score
7. Train K-Means Model
8. Save Model using Pickle
9. Deploy using Flask

---

## 📈 Choosing the Best Value of K

### Elbow Method

The Elbow Method was used to determine the optimal number of clusters.

**Optimal K = 2**

### Silhouette Score

| K | Score |
|---|------:|
| **2** | **0.5408** |
| 3 | 0.3246 |
| 4 | 0.3084 |
| 5 | 0.2672 |
| 6 | 0.2626 |
| 7 | 0.2596 |
| 8 | 0.2681 |
| 9 | 0.2635 |
| 10 | 0.2667 |

The highest Silhouette Score was obtained at **K = 2**, confirming it as the optimal number of clusters.

---

## 📊 Cluster Evaluation

| Cluster | Genuine | Fraud |
|---------|---------:|------:|
| 0 | 40,000 | 40 |
| 1 | 0 | 9,960 |

### Performance

- Genuine Transaction Detection: **100%**
- Fraud Detection: **99.6%**

> **Note:** These results are based on a synthetic dataset created for learning and demonstration purposes.

---

## 💻 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Fraud_Detection.git
```

### Move to Project Folder

```bash
cd Fraud_Detection
```

### Install Required Libraries

```bash
pip install -r requirment.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## 🖥️ Application Pages

### Home Page

- Enter transaction details.
- Click **Predict Transaction**.

### Result Page

Displays one of the following results:

- ✅ Genuine Transaction
- ⚠️ Fraudulent Transaction

---

## 📦 Saved Model Files

The trained machine learning model is stored inside the **model** folder.

| File | Purpose |
|------|---------|
| `kmeans_model.pkl` | Trained K-Means model |
| `scaler.pkl` | StandardScaler used during preprocessing |

These files are loaded directly by **app.py** for prediction without retraining the model.

---

## 📚 Future Improvements

- Real-world banking transaction dataset
- DBSCAN clustering
- Isolation Forest
- Anomaly Detection
- Interactive dashboard
- Charts and analytics
- User authentication
- Transaction history
- Model comparison

---

## 👨‍💻 Author

**Manas Sharma**

Engineering Student

**Interests**

- Machine Learning
- Artificial Intelligence
- Data Science
- Flask Development
- Java & Python

---

## 📄 License

This project is created for educational and learning purposes.