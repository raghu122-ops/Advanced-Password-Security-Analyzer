from flask import Flask, render_template, request, jsonify
import re
import math
import hashlib
import requests

app = Flask(__name__)


def password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[!@#$%^&*()]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def entropy(password):

    charset = 0

    if re.search("[a-z]", password):
        charset += 26
    if re.search("[A-Z]", password):
        charset += 26
    if re.search("[0-9]", password):
        charset += 10
    if re.search("[!@#$%^&*()]", password):
        charset += 32

    if charset == 0:
        return 0

    return round(len(password) * math.log2(charset), 2)


def crack_time(ent):

    guesses = 2 ** ent
    seconds = guesses / 1000000000

    if seconds < 60:
        return "Seconds"
    elif seconds < 3600:
        return "Minutes"
    elif seconds < 86400:
        return "Hours"
    elif seconds < 31536000:
        return "Days"
    else:
        return "Years"


# Breach check using HaveIBeenPwned API
def check_breach(password):

    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()

    prefix = sha1[:5]
    suffix = sha1[5:]

    url = "https://api.pwnedpasswords.com/range/" + prefix

    response = requests.get(url)

    hashes = (line.split(":") for line in response.text.splitlines())

    for h, count in hashes:
        if h == suffix:
            return int(count)

    return 0


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():

    data = request.get_json()
    password = data["password"]

    strength = password_strength(password)

    ent = entropy(password)

    time = crack_time(ent)

    breach_count = check_breach(password)

    if breach_count > 0:
        breach = f"⚠ WARNING: Password found {breach_count} times in data breaches"
    else:
        breach = "Safe – Not found in breach database"

    suggestions = []

    if len(password) < 8:
        suggestions.append("Increase password length")

    if not re.search("[A-Z]", password):
        suggestions.append("Add uppercase letters")

    if not re.search("[0-9]", password):
        suggestions.append("Add numbers")

    if not re.search("[!@#$%^&*()]", password):
        suggestions.append("Add special characters")

    if len(suggestions) == 0:
        suggestions.append("Password is secure")

    return jsonify({
        "strength": strength,
        "entropy": ent,
        "time": time,
        "breach": breach,
        "suggestions": suggestions
    })


if __name__ == "__main__":
    app.run(debug=True)