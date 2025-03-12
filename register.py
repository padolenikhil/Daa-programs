import mysql.connector
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# MySQL connection details
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'bookmyshow'
}

@app.route('/register', methods=['POST'])
def register():
    # Get form data
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    try:
        # Establish connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert data into MySQL
        query = "INSERT INTO users (name, username, password, email) VALUES (%s, %s, %s, %s)"
        values = (name, username, password, email)
        cursor.execute(query, values)

        # Commit the transaction
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        return redirect('/success')

    except mysql.connector.Error as err:
        return f"Error: {err}"

@app.route('/success')
def success():
    return "Registration successful!"

if __name__ == "__main__":
    app.run(debug=True)
