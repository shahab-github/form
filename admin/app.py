from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database Configuration
db = mysql.connector.connect(
    host='localhost',
    user='python',
    password='password',
    database='myusers'
)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Save user data to database
@app.route('/submit-form', methods=['POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        mobile_num = request.form['mobile_num']
        email = request.form['email']

        # Insert user data into database
        cursor = db.cursor()
        sql = "INSERT INTO users (first_name, last_name, mobile_num, email) VALUES (%s, %s, %s, %s)"
        val = (first_name, last_name, mobile_num, email)
        cursor.execute(sql, val)
        db.commit()

        return render_template('success.html')

# Admin page to display user list
@app.route('/admin')
def admin():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    return render_template('admin.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

