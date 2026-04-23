from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import sys
import webbrowser

DETECT_TEXT = "buy tickets"
URL = "https://shop.royalchallengers.com/ticket"
CHECK_INTERVAL = 30 # seconds between checks
found_once = False  # Flag to stop checking after first detection

# 🔧 Create and configure Selenium Chrome driver
def make_driver() -> webdriver.Chrome:

    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280,800")

    # Reduce Selenium detection
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    driver.minimize_window()  # keep it hidden in background
    return driver


# 🌐 Initialize driver once (persistent session)
driver = make_driver()

# 🧹 Normalize button text (clean + lowercase)
def normalize_text(text: str) -> str:
    return " ".join(text.split()).strip().lower()


# 🔔 Trigger alert + open real Chrome tab
def alert_and_open():
    
    global driver, found_once

    if found_once:
        return  # prevent duplicate triggers

    found_once = True

    # 🔊 Sound alert (Windows)
    try:
        import winsound
        for _ in range(2):
            winsound.Beep(1000, 400)
            time.sleep(0.15)
    except Exception:
        print("\a\a\a", flush=True)  # fallback beep

    # ❌ Close Selenium browser
    try:
        driver.quit()
        print("🔴 Closed debug Chrome.")
    except Exception:
        pass

    # 🌐 Open real Chrome (user session)
    webbrowser.open_new_tab(URL)
    print("🌐 Opened in your Chrome — GO BUY NOW!!")


# 🔄 Restart driver if crash occurs
def restart_driver():
    
    global driver
    try:
        driver.quit()
    except Exception:
        pass

    print("🔄 Restarting driver...")
    time.sleep(4)

    # create new driver
    driver = make_driver()

    # ✅ load your URL again
    driver.get(URL)

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# 🔍 Check ticket availability
def check() -> bool:
    
    global driver

    try:
        driver.get(URL)

        # Wait for page to load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Get all clickable elements
        elements = driver.find_elements(By.XPATH, "//button | //a")

        for el in elements:
            try:
                text = normalize_text(el.text)
            except Exception:
                continue

            if not text:
                continue

            # 🎯 Ticket detection logic
            if (DETECT_TEXT in text) and el.is_displayed():
                print(f"🔥 TICKETS AVAILABLE → '{el.text.strip()}'")
                return True

        print("❌ Not available yet")
        return False

    except Exception as e:
        # Handle driver crash gracefully
        err_first_line = str(e).splitlines()[0] if str(e) else "unknown"
        print(f"⚠️ Driver error: {err_first_line}")
        restart_driver()
        return False


# ⏳ Countdown timer between checks
def countdown(seconds: int):
    
    
    for i in range(seconds, 0, -1):
        print(f"\r⏳ Next check in: {i:02d}s ", end="", flush=True)
        time.sleep(1)
    print("\r🔄 Checking now...          ", flush=True)


# 🚀 Script start
print(f"\n🚀 Monitoring: {URL}")
print(f"   Interval : every {CHECK_INTERVAL}s")
print("   Chrome   : minimized debug window (Do not close the chrome window.)\n")


# 🔁 Main loop
try:
    while not found_once:
        print(f"\n🕒 {datetime.now().strftime('%H:%M:%S')}", flush=True)

        if check():
            alert_and_open()
            break  # stop after first detection

        countdown(CHECK_INTERVAL)


# 🛑 Manual stop
except KeyboardInterrupt:
    print("\n\n🛑 Stopped by user.")


# 🧹 Cleanup
finally:
    try:
        driver.quit()
    except Exception:
        pass
    sys.exit(0)
