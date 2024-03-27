from flask import Flask, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    if 'response' not in session:
        session['response'] = ""

    if request.method == 'POST':
        session_id = request.values.get("sessionId", None)
        service_code = request.values.get("serviceCode", None)
        phone_number = request.values.get("phoneNumber", None)
        text = request.values.get("text", "")

        if text == '':
            session['response'] = "CON Are you persons with disability or pregnant?\n"
            session['response'] += "Reply with:\n"
            session['response'] += "1. Yes\n"
            session['response'] += "2. No"

        elif text == '1':
            session['response'] = "CON Please specify:\n"
            session['response'] += "1. Disabled\n"
            session['response'] += "2. Pregnant"

        elif text == '2':
            session['response'] = "CON Proceeding to the main menu:\n"
            session['response'] += "1. Sustainable Farming Education\n"
            session['response'] += "2. Carbon Credit Awareness\n"
            session['response'] += "3. Local Resource Mapping\n"
            session['response'] += "4. Community Engagement"

        elif text == '1*1':
            session['response'] = "CON Since you are disabled, we recommend crops that require less physical effort to maintain:\n"
            session['response'] += "1. Mushroom farming\n"
            session['response'] += "2. Hydroponic farming\n"
            session['response'] += "3. Vertical farming\n"
            session['response'] += "4. Beekeeping"

        elif text == '1*2':
            session['response'] = "CON Since you are pregnant, we recommend crops that require less attention on the farm:\n"
            session['response'] += "1. Sweet Potatoes\n"
            session['response'] += "2. Pumpkins\n"
            session['response'] += "3. Green Beans\n"
            session['response'] += "4. Lettuce"

    return session.get('response', '')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))
