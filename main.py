from flask import Flask, request, render_template
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

app = Flask(__name__)

# ======================
# Translations Dictionary
# ======================
translations = {
    "hi": {
        "Recommended Crop": "अनुशंसित फसल",
        "Sowing Date": "बुवाई की तारीख",
        "Irrigation Date": "सिंचाई की तारीख",
        "Harvest Date": "कटाई की तारीख",
        "Crop Calendar": "फसल कैलेंडर",
        "Suggested Crop Rotation Options": "फसल चक्र विकल्प"
    },
    "te": {
        "Recommended Crop": "సిఫార్సు చేసిన పంట",
        "Sowing Date": "విత్తె తేదీ",
        "Irrigation Date": "పాలింపు తేదీ",
        "Harvest Date": "కోత తేదీ",
        "Crop Calendar": "పంట క్యాలెండర్",
        "Suggested Crop Rotation Options": "పంట మార్పిడి సూచనలు"
    },
    "kn": {
        "Recommended Crop": "ಶಿಫಾರಸು ಮಾನ್ಯ ಬೆಳೆಯು",
        "Sowing Date": "ಬಿತ್ತನೆ ದಿನಾಂಕ",
        "Irrigation Date": "ನೆರೆಯ ದಿನಾಂಕ",
        "Harvest Date": "ಕಟಾವು ದಿನಾಂಕ",
        "Crop Calendar": "ಬೆಳೆ ಕ್ಯಾಲೆಂಡರ್",
        "Suggested Crop Rotation Options": "ಬೆಳೆ ಪರಿವರ್ತನೆ ಆಯ್ಕೆಗಳು"
    }
}

# ======================
# Crop Calendar Function
# ======================
def get_crop_schedule(crop_name):
    with open("crop_calendar.json", "r") as f:
        crop_data = json.load(f)
    if crop_name not in crop_data:
        return None
    today = datetime.now()
    schedule = crop_data[crop_name]
    return {
        "sowing": today.strftime("%Y-%m-%d"),
        "irrigation": (today + timedelta(days=schedule["irrigation_days"])).strftime("%Y-%m-%d"),
        "harvesting": (today + timedelta(days=schedule["harvesting_days"])).strftime("%Y-%m-%d")
    }

# ======================
# Email Notification
# ======================
def send_email_alert(user_email, crop_name, schedule):
    sender_email = EMAIL_USER
    sender_password = EMAIL_PASS

    subject = f"Your Crop Calendar for {crop_name.capitalize()}"
    body = f"""
    Dear Farmer,

    Here's your schedule for {crop_name.capitalize()}:

    🌱 Sowing Date: {schedule['sowing']}
    💧 Irrigation Date: {schedule['irrigation']}
    🌾 Harvest Date: {schedule['harvesting']}

    Wishing you a great harvest!
    - Agro Recommendation System
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = user_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print(f"✅ Email sent to {user_email}")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

# ======================
# Crop Rotation Suggestion
# ======================
def get_crop_rotation_suggestions(previous_crop):
    with open("rotation_rules.json", "r") as f:
        rules = json.load(f)
    return rules.get(previous_crop, [])

# ======================
# Routes
# ======================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ndvi = float(request.form['ndvi'])
    rainfall = float(request.form['rainfall'])
    moisture = float(request.form['moisture'])
    user_email = request.form['email']
    prev_crop = request.form['prev_crop']
    lang = request.form.get('lang', 'en')
    lang_dict = translations.get(lang, {})

    # Simple Rule-based Prediction
    if ndvi > 0.5 and rainfall > 100:
        predicted_crop = "rice"
    elif ndvi > 0.3:
        predicted_crop = "wheat"
    else:
        predicted_crop = "millet"

    # Calendar & Email
    schedule = get_crop_schedule(predicted_crop)
    if schedule:
        send_email_alert(user_email, predicted_crop, schedule)

    # Rotation Suggestion
    rotation_suggestions = get_crop_rotation_suggestions(prev_crop)

    return render_template("result.html",
                           crop=predicted_crop,
                           schedule=schedule,
                           ndvi=ndvi,
                           rainfall=rainfall,
                           moisture=moisture,
                           prev_crop=prev_crop,
                           rotation=rotation_suggestions,
                           lang_dict=lang_dict)

if __name__ == '__main__':
    app.run(debug=True)
