from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo
import bcrypt

# Initialize the Flask app and configure MongoDB URI
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/your_database'  # Replace with your MongoDB URI
mongo = PyMongo(app)

# Route for the homepage (login form)
@app.route('/')
def home():
    return render_template('login.html')

# Route to handle login logic
@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form
    username = request.form['username']
    password = request.form['password']
    
    # Fetch user from the MongoDB users collection
    user = mongo.db.users.find_one({'username': username})
    
    if user:
        # Check if the entered password matches the hashed password in MongoDB
        if bcrypt.checkpw(password.encode('utf-8'), user['password']):
            # Password matches, set session and redirect to a protected page
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials!', 'danger')
    else:
        flash('User not found!', 'danger')
    
    return redirect(url_for('home'))

# Route for dashboard (protected page after login)
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    return f'Welcome {session["username"]} to the Dashboard!'

# Route for registering a new user (optional)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the user already exists
        if mongo.db.users.find_one({'username': username}):
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        
        # Hash the password before saving to MongoDB
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # Save the user to MongoDB
        mongo.db.users.insert_one({'username': username, 'password': hashed_password})
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('home'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
