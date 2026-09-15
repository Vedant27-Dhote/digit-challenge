import os
from flask import Flask, render_template, request, jsonify, abort

app = Flask(__name__)

# This is a GAME challenge code only. Do not use a real phone/device password.
ROOM_CODE = os.environ.get("ROOM_CODE", "BROOKLYN123")

# In-memory storage: disappears when the server restarts.
secret_code = None

def valid_code(code):
    return (
        isinstance(code, str)
        and len(code) == 4
        and code.isdigit()
        and len(set(code)) == 2
        and all(code.count(d) == 2 for d in set(code))
    )

def check_room(room):
    if room != ROOM_CODE:
        abort(404)

@app.get("/")
def home():
    return render_template("home.html", room=ROOM_CODE)

@app.get("/friend")
def friend():
    room = request.args.get("room", "")
    check_room(room)
    return render_template("friend.html", room=room)

@app.post("/set-secret")
def set_secret():
    global secret_code
    room = request.form.get("room", "")
    code = request.form.get("code", "")
    check_room(room)

    if not valid_code(code):
        return render_template(
            "friend.html",
            room=room,
            error="Use exactly 4 digits with two different digits, each repeated twice (e.g. 1122, 1212, 1221)."
        )

    secret_code = code
    return render_template("friend_done.html")

@app.get("/guess")
def guess():
    room = request.args.get("room", "")
    check_room(room)
    return render_template("guess.html", room=room)

@app.post("/check-digit")
def check_digit():
    room = request.form.get("room", "")
    digit = request.form.get("digit", "")
    position = request.form.get("position", "")

    check_room(room)

    if secret_code is None:
        return jsonify(ok=False, message="Your friend has not set the challenge code yet.")

    if position not in {"0", "1", "2", "3"}:
        return jsonify(ok=False, message="Invalid position.")

    if len(digit) != 1 or not digit.isdigit():
        return jsonify(ok=False, message="Enter exactly one digit.")

    correct = digit == secret_code[int(position)]
    return jsonify(ok=True, correct=correct)

@app.get("/status")
def status():
    room = request.args.get("room", "")
    check_room(room)
    return jsonify(set=secret_code is not None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
