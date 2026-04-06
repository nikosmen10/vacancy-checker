# web-monitor-alert-system

Automated Python script that monitors a PerfectGym booking portal for available spots in a specific swim class and sends an email notification when a vacancy appears.

## Features

- Scrapes live class availability from PerfectGym portal
- Runs automatically every 30 minutes
- Sends email alert when a spot opens
- Runs headless (no visible browser window)
- Easy to adapt to any class or portal

## Tech Stack

- Python 3.12
- Selenium (web scraping)
- Webdriver Manager (automatic Chrome driver)
- Schedule (automated timing)
- SMTP (email notifications)

## How It Works

1. Script opens the PerfectGym booking page in a headless browser
2. Reads the page and looks for the target class
3. If spots are available, sends an email notification immediately
4. Repeats every 30 minutes automatically

## Setup

1. Clone the repo
   git clone https://github.com/nikosmen10/vacancy-checker.git
   cd vacancy-checker

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install selenium webdriver-manager schedule

4. Configure your settings in checker.py
   - CLASS_NAME: the class you want to monitor
   - EMAIL_FROM: your Gmail address
   - EMAIL_PASSWORD: your Gmail app password
   - EMAIL_TO: where to send alerts

5. Run the script
   python checker.py

## Configuration

| Variable | Description |
|---|---|
| `URL` | PerfectGym portal URL |
| `CLASS_NAME` | Name of class to monitor |
| `EMAIL_FROM` | Sender Gmail address |
| `EMAIL_PASSWORD` | Gmail app password |
| `EMAIL_TO` | Recipient email address |

## Output Example
```
========================================
  Vacancy Checker Started
  Monitoring: Wetlanders
  Checking every 30 minutes
  Press Ctrl+C to stop
========================================
[15:48:18] Checking Wetlanders...
✅ Vacancy found! 2 spot(s) available!
📧 Email sent!
```

## Author

Nikos — Field Engineer & Python Developer
