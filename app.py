from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def is_armstrong(n):
    n = abs(n)  # Convert to positive for digit processing
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == abs(n)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def get_digit_sum(n):
    return sum(int(d) for d in str(abs(n)))  # Use absolute value

def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}/math?json"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.json().get("text", "No fun fact available.")
    except requests.exceptions.RequestException:
        return "No fun fact available."

@app.route("/api/classify-number", methods=["GET"])
def classify_number():
    num = request.args.get("number")
    
    if not num or (num[0] == '-' and not num[1:].isdigit()) or (num[0] != '-' and not num.isdigit()):
        return jsonify({"number": num, "error": True}), 400
    
    num = int(num)
    properties = ["armstrong"] if is_armstrong(num) else []
    properties.append("odd" if num % 2 else "even")

    response_data = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": get_digit_sum(num),
        "fun_fact": get_fun_fact(num)
    }
    return jsonify(response_data), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
