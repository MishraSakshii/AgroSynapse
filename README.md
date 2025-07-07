# AgriSynapse: Smart Crop Planner & Advisory System

**AgriSynapse** is an intelligent agricultural assistant that helps farmers and agri-enthusiasts make informed decisions on:
- **Which crop to grow next** based on rotation patterns
- **When to sow, grow, and harvest** using an interactive crop calendar
- **Multi-language support** for accessibility
- **Email alerts & reminders** for optimal crop actions

---

## Features

### Crop Recommendation Engine
- Suggests the best crop to grow based on:
  - Location
  - Soil condition
  - Seasonal rotation history

### Crop Calendar
- Shows phase-wise crop timelines:
  - Sowing window
  - Growth duration
  - Harvest window
- Dynamically updates based on selected crop & region

### Multi-language UI
- Supports **regional languages** for easier access
- Automatically adapts to selected language preference

### Email Notification System
- Users enter their **email ID** once
- System sends alerts and tips:
  - Upcoming sowing/harvest dates
  - Weather updates
  - Crop-specific care suggestions

---

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/agrosynapse.git
cd agrosynapse
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create `.env` file
```
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_app_password
```

### 4. Run the App
```bash
python app.py
```
Visit: [http://localhost:5000](http://localhost:5000)

---

## Data Sources
- Crop seasonality from Indian Agri Dept
- Rotation practices from ICAR datasets
- Language mappings via Google Translate API / local dictionaries

---

## How Notifications Work
- User inputs email ID once
- Backend schedules email reminders via SMTP
- Timed reminders based on calendar logic per crop

---

## To-Do / Upcoming Features
- [ ] SMS alert integration
- [ ] Weather-based auto-reminders
- [ ] Voice assistant integration (for kiosk use)

---

## Use Cases
- Farmers planning rotational cropping
- Students learning crop cycles
- NGOs or gov orgs assisting rural agriculture

---

## Acknowledgements
- ICAR for rotation & yield references
- Flask + SMTP for web & mail integration

---

## License
MIT License © Sakshi Mishra


