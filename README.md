Web Portal Monitor & Alert System

Automated Python tool that monitors any web portal for a specific condition and sends an instant email notification the moment it's met — no manual checking required.
Built for scenarios where a web interface doesn't offer a native API or webhook, but you still need to react to changes in real time.

Features

Monitors live, JavaScript-rendered web pages using a headless browser
Runs automatically on a configurable interval (default: every 30 minutes)
Sends an instant email alert when the target condition is detected
Runs fully headless — no visible browser window, no manual interaction
Easily configurable for any portal, any target condition


Use cases

Equipment & asset monitoring — track status changes on supplier or manufacturer portals
Procurement & inventory — get alerted when a part or product becomes available
Booking & scheduling systems — detect open slots in any web-based booking platform
Industrial dashboards — monitor web-based SCADA or reporting pages for state changes
Any web portal without an API — if it renders in a browser, this tool can watch it


Tech stack
ToolPurposePython 3.12Core languageSeleniumHeadless browser automationWebdriver ManagerAutomatic Chrome driver managementScheduleAutomated timing loopSMTPEmail alert delivery

How it works

Script opens the target portal in a headless Chrome browser
Reads the page and checks for the configured condition
If the condition is met, sends an email notification immediately
Repeats on the configured interval automatically


Setup
1. Clone the repo
bashgit clone https://github.com/nikosmen10/web-monitor-alert-system.git
cd web-monitor-alert-system
2. Create a virtual environment
bashpython -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
3. Install dependencies
bashpip install selenium webdriver-manager schedule
4. Configure your settings in checker.py
VariableDescriptionURLTarget portal URL to monitorTARGET_NAMEThe condition or item to watch forCHECK_INTERVALHow often to check, in minutes (default: 30)EMAIL_FROMSender Gmail addressEMAIL_PASSWORDGmail app passwordEMAIL_TORecipient email address
5. Run
bashpython checker.py

Example output
========================================
  Web Monitor Started
  Watching: [TARGET_NAME]
  Checking every 30 minutes
  Press Ctrl+C to stop
========================================
[15:48:18] Checking status...
✅ Condition met! Sending alert...
📧 Email sent!

Adapting to your use case
The core monitoring logic is in checker.py. To point it at a different portal:

Update URL to your target page
Update TARGET_NAME to match what you're looking for
Adjust the page-reading logic to match the structure of your target site

The scheduling, headless browser setup, and email delivery require no changes.

Author
Nikos — Industrial IoT & Automation Engineer | Robotics MSc
Field service background in industrial processing equipment (separators, homogenizers, heat exchangers).
I build Python automation tools for engineering and manufacturing teams.
