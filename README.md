# 🛫 Flight Satisfaction Prediction Web App

This is a simple yet effective machine learning-powered web application built using **Flask** and integrated with a **MySQL database**.<br>  
It predicts whether a passenger is **satisfied** or **dissatisfied** based on flight experience inputs like delay, cleanliness, baggage handling, etc.<br>  
All predictions and user inputs are logged in a database for tracking and analysis.

---

## 📦 Requirements

Install the required libraries using:

```bash
pip install streamlit python-dotenv google-generativeai pillow
```

---

## 🚀 How to Run
1. Ensure MySQL is installed and running.
2. Create a database and table (see below 👇).
3. Then, to run the Flask app locally:
```bash
python app.py
```

---

## 🧠 How It Works
1. A trained Logistic Regression model (logistic_regression.lb) is loaded.
2. Users fill out a form with flight experience details.
3. On submission, data is sent to the model for prediction.
4. The result (SATISFIED or DISATISFIED) is shown and saved in the MySQL database.

---

## 🛠️ Database Setup
### 1. Create a database:
```bash
CREATE DATABASE niteshdb;
```
### 2. Create a predictions table:
```bash
CREATE TABLE predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    flight_distance INT,
    infligth_entertainment INT,
    baggage_handling INT,
    cleanliness INT,
    departure_delay INT,
    arrival_delay INT,
    gender INT,
    customer_type INT,
    travel_type INT,
    class_Type VARCHAR(20),
    prediction VARCHAR(20)
);
```
### 3. Update your DB credentials in app.py:
```bash
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
```

---

## ✨ Example Use Cases
### ✅ Predict Satisfaction
• Input: Age: 29, Flight Distance: 1200, Cleanliness: 4, Delay: 5 mins
• Class: ECO
• Output: "SATISFIED"

### ❌ Predict Dissatisfaction
• Input: Age: 52, Delay: 80 mins, Entertainment: 1, Baggage Handling: 2
• Class: BUSINESS
• Output: "DISATISFIED"

---

## 📂 File Structure
```bash
flight-app/
│
├── templates/
│   ├── home.html
│   ├── project.html
│   └── output.html
│
├── logistic_regression.lb    # Trained ML model
├── app.py                    # Main Flask backend
└── README.md                 # Documentation
```



## 📌 Notes
• Ensure your model file (logistic_regression.lb) is in the root directory.<br>
• You can expand this app with features like user login, visualizations, or admin analytics panel.<br>
• Test the form carefully for edge case values (e.g., high delays or 0 cleanliness).<br>

