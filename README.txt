# 4-Digit Challenge Game

This is a consent-based guessing game. It is NOT for collecting real phone/device passwords.

## Files
- app.py
- requirements.txt
- templates/home.html
- templates/friend.html
- templates/friend_done.html
- templates/guess.html

## Local test
Install Python, then:

    pip install -r requirements.txt
    python app.py

Open:
    http://127.0.0.1:5000/

## Deploy on Render
1. Put these files in a GitHub repository.
2. On Render, create a New > Web Service and connect the repository.
3. Runtime: Python 3
4. Build command:
       pip install -r requirements.txt
5. Start command:
       gunicorn app:app
6. Choose the Free plan for a short hobby test.
7. Add an environment variable:
       ROOM_CODE
   Set it to a random value, for example:
       VEDANT-7F3K9Q
8. Deploy.

Then use:
    https://YOUR-SERVICE.onrender.com/friend?room=YOUR_ROOM_CODE

Send that Friend link to your friend.

For your guessing page:
    https://YOUR-SERVICE.onrender.com/guess?room=YOUR_ROOM_CODE

IMPORTANT:
- The secret is held only in server memory.
- A server restart clears it.
- Free hosting may sleep/restart.
- Do not use this to collect a real phone, account, banking, or other credential.
