from flask import Flask, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Dictionary to store crop recommendations for each main menu option
recommendations = {
    "1": "1. Mushroom farming\n2. Hydroponic farming\n3. Vertical farming\n4. Beekeeping",
    "2": "1. Avocado\n2. Citrus fruits\n3. Bamboo\n4. Agroforestry",
    "3": "1. Water resources\n2. Soil health\n3. Biodiversity mapping\n4. Renewable energy sources",
    "4": "1. Join local farming cooperatives\n2. Participate in farmer markets\n3. Community gardens\n4. Agricultural education programs"
}

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

        elif text == '1*1':
            session['response'] = "CON Since you are disabled, we recommend crops that require less physical effort to maintain:\n"
            session['response'] += recommendations['1']
            session['response'] += "\n0. Back to Main Menu"

        elif text == '1*2':
            session['response'] = "CON Since you are pregnant, we recommend crops that require less attention on the farm:\n"
            session['response'] += recommendations['2']
            session['response'] += "\n0. Back to Main Menu"

        elif text == '2' or text == '3' or text == '4':
            session['response'] = "CON Main Menu:\n"
            session['response'] += "1. Sustainable Farming Education\n"
            session['response'] += "2. Carbon Credit Awareness\n"
            session['response'] += "3. Local Resource Mapping\n"
            session['response'] += "4. Community Engagement"
            session['response'] += "\n0. Return to Previous Menu"

        elif text == '0':
            session['response'] = "CON Returning to the previous menu:\n"
            session['response'] += "1. Sustainable Farming Education - Learn about sustainable farming practices and techniques.\n"
            session['response'] += "2. Carbon Credit Awareness - Understand the benefits and methods of carbon credits in agriculture.\n"
            session['response'] += "3. Local Resource Mapping - Explore available resources in your locality for farming.\n"
            session['response'] += "4. Community Engagement - Get involved in community farming initiatives and programs."

    return session.get('response', '')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))
