from flask import Flask, render_template, url_for, request
import joblib
from flask_mysqldb import MySQL

model = joblib.load('logistic_regression.lb')
app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'nit2403@'
app.config['MYSQL_DB'] = 'niteshdb'

# Initialize MySQL object
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        age = int(request.form['age'])
        flight_distance = int(request.form['flight_distance'])
        infligth_entertainment = int(request.form["inflight-entertainment"])
        baggage_handling = int(request.form["baggage-handling"])
        cleanliness = int(request.form["cleanliness"])
        departure_delay = int(request.form["departure_delay"])
        arrival_delay = int(request.form["arrival_delay"])
        gender = int(request.form["gender"])
        customer_type = int(request.form["customer-type"])
        travel_type = int(request.form["travel-type"])
        class_Type = request.form["class-type"]
        Class_Eco = 0
        Class_Eco_Plus = 0
        if class_Type == 'ECO':
            Class_Eco = 1
            Class_Eco_Plus = 0
        elif class_Type == 'ECO_PLUS':
            Class_Eco = 0
            Class_Eco_Plus = 1
        else:
            Class_Eco = 0
            Class_Eco_Plus = 0
        UNSEEN_DATA = [[age, flight_distance, infligth_entertainment, baggage_handling,
                       cleanliness, departure_delay, arrival_delay, gender,
                       customer_type, travel_type, Class_Eco, Class_Eco_Plus]]

        prediction = model.predict(UNSEEN_DATA)[0]
        print(prediction)
        labels = {'1': "SATISFIED", '0': "DISATISFIED"}

        # Save the prediction to the database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO predictions (age, flight_distance, infligth_entertainment, baggage_handling, cleanliness, departure_delay, arrival_delay, gender, customer_type, travel_type, class_Type, prediction) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (age, flight_distance, infligth_entertainment, baggage_handling, cleanliness, departure_delay, arrival_delay, gender, customer_type, travel_type, class_Type, labels[str(prediction)]))
        mysql.connection.commit()
        cur.close()

        return render_template('output.html', output=labels[str(prediction)])

if __name__ == "__main__":
    app.run(debug=True)