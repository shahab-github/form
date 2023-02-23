from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Get the form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    mobile_num = request.form['mobile_num']
    email = request.form['email']

    # Connect to the database
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='myusers'
    )

    cursor = connection.cursor()

    # Insert the data into the users table
    sql = "INSERT INTO users (first_name, last_name, mobile_num, email) VALUES (%s, %s, %s, %s)"
    val = (first_name, last_name, mobile_num, email)
    cursor.execute(sql, val)

    # Commit the changes and close the cursor and connection
    connection.commit()
    cursor.close()
    connection.close()

    return 'Data inserted successfully into MySQL table'

if __name__ == '__main__':
    app.run()
