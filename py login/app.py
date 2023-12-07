from flask import Flask, render_template, request, redirect,url_for
import mysql.connector

app = Flask(__name__)

def authenticate(username, password):
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='baljinder@100',
            database='mydb'
        )

        cursor = connection.cursor()

        # Check if the user exists
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            return True
        else:
            return False

    except mysql.connector.Error as err:
        print("Database error: {}".format(err))
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        if authenticate(username, password):
          
          return redirect(url_for('dashboard'))
        else:
             return render_template('index.html', error='Invalid credentials')
@app.route('/dashboard')
def dashboard():
    # Render the dashboard template
    return render_template('dashboard.html')
if __name__ == '__main__':
    app.run(debug=True)
