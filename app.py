from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # This is for flash messages and session management

# Dummy user data for login purposes
users = {"admin": "password123"}

@app.route('/')
def welcome():
    return render_template('welcome.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if username already exists
        if username in users:
            flash("Username already taken. Please choose a different username.", "danger")
            return redirect(url_for('register'))

        # Check if passwords match
        if password != confirm_password:
            flash("Passwords do not match. Please try again.", "danger")
            return redirect(url_for('register'))

        # Store the new user (you can hash the password for security in a real app)
        users[username] = password
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('login'))  # Redirect to the login page after successful registration

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login here (for now, just redirecting to tasks)
        return redirect(url_for('tasks'))
    return render_template('login.html')

@app.route('/tasks')
def tasks():
    return "<h1>Welcome to your tasks</h1>"

if __name__ == '__main__':
    app.run(debug=True)