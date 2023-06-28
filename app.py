from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if request.method == 'POST':
        user_guess = int(request.form['guess'])
        correct_number = random.randint(1, 2)
        if user_guess == correct_number:
            message = "Congratulations! You guessed the correct number."
        elif user_guess < correct_number:
            message = "Sorry, your guess is too low. Please try again."
        else:
            message = "Sorry, your guess is too high. Please try again."
        return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

