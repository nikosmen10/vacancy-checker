from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import smtplib
from email.mime.text import MIMEText
import time
import schedule

# --- CONFIG ---
URL        = "https://cockburnarc.perfectgym.com.au/ClientPortal2/#/Groups/1?vacancies=1"
CLASS_NAME = "Wetlanders"

# --- EMAIL CONFIG ---
EMAIL_FROM     = "djmys7@gmail.com"
EMAIL_PASSWORD = "nvelxusvlfqvnxcg"
EMAIL_TO       = "djmys7@gmail.com"

def send_email(subject, body):
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"]    = EMAIL_FROM
        msg["To"]      = EMAIL_TO
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            server.send_message(msg)
        print("📧 Email sent!")
    except Exception as e:
        print(f"Email failed: {e}")

def check_vacancies():
    print(f"\n[{time.strftime('%H:%M:%S')}] Checking {CLASS_NAME}...")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get(URL)
        time.sleep(6)

        page_text = driver.find_element(By.TAG_NAME, "body").text

        if CLASS_NAME.lower() not in page_text.lower():
            print(f"❌ {CLASS_NAME} not found — no vacancy today.")
            return

        # Parse spots
        lines       = page_text.split("\n")
        spots       = None
        found_class = False

        for line in lines:
            if CLASS_NAME.lower() in line.lower():
                found_class = True
            if found_class and "Spots left:" in line:
                try:
                    spots = int(line.replace("Spots left:", "").strip())
                except:
                    spots = None
                break

        if found_class and spots and spots > 0:
            message = (
                f"🏊 VACANCY ALERT!\n\n"
                f"{CLASS_NAME} has {spots} spot(s) available!\n\n"
                f"Book now: {URL}"
            )
            print(f"✅ Vacancy found! {spots} spot(s) available!")
            send_email(f"🏊 {CLASS_NAME} has a spot!", message)

        elif found_class and spots == 0:
            print(f"❌ {CLASS_NAME} found but fully booked.")
        else:
            print(f"⚠️ {CLASS_NAME} found but couldn't read spot count.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

def main():
    print("=" * 40)
    print(f"  Vacancy Checker Started")
    print(f"  Monitoring: {CLASS_NAME}")
    print(f"  Checking every 30 minutes")
    print(f"  Press Ctrl+C to stop")
    print("=" * 40)

    # Run once immediately
    check_vacancies()

    # Then every 30 minutes
    schedule.every(30).minutes.do(check_vacancies)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()