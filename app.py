from flask import Flask, render_template, request, jsonify, session
import _secret_backend as backend
import secrets
import os

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    data = request.json or {}
    difficulty = data.get('difficulty', 'medium')
    
    # Define difficulty ranges
    ranges = {
        'easy': (1, 50),
        'medium': (1, 100),
        'hard': (1, 500)
    }
    
    low, high = ranges.get(difficulty, (1, 100))
    secret_number = backend._get_secret_number(low, high)
    
    session['secret_number'] = secret_number
    session['attempts'] = 0
    session['range'] = [low, high]
    
    return jsonify({
        "success": True, 
        "message": f"New {difficulty} game started!",
        "low": low,
        "high": high
    })

@app.route('/guess', methods=['POST'])
def guess():
    data = request.json
    guess = data.get('guess')
    
    if guess is None or not isinstance(guess, int):
        return jsonify({"success": False, "message": "Invalid input"}), 400
    
    secret_number = session.get('secret_number')
    if secret_number is None:
        return jsonify({"success": False, "message": "Game not started"}), 400
    
    low, high = session.get('range', [1, 100])
    
    if guess < low or guess > high:
        return jsonify({"success": False, "message": f"Please guess a number between {low} and {high}."}), 400

    session['attempts'] = session.get('attempts', 0) + 1
    result = backend._evaluate_guess(guess, secret_number)
    
    response = {
        "success": True,
        "result": result,
        "attempts": session['attempts']
    }
    
    if result == 0:
        response["message"] = f"Congratulations! You've guessed the correct number {secret_number} in {session['attempts']} attempts."
        # Reset game session
        session.pop('secret_number', None)
    elif result == -1:
        response["message"] = "Too low! Try again."
    else:
        response["message"] = "Too high! Try again."
        
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
