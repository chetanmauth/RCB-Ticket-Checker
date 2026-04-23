# 🎟️ RCB-Ticket-Checker
RCB Ticket Availability Checker is a lightweight automation tool that continuously monitors the official Royal Challengers Bengaluru ticket website and instantly alerts the user when tickets become available.

A Python-based automation tool that continuously monitors the official Royal Challengers Bengaluru (RCB) ticket website and instantly alerts you when tickets become available.


<img src="[https://github.com/chetanmauth/Geoserver/blob/main/images/geoImage.jpeg](https://github.com/chetanmauth/RCB-Ticket-Checker/blob/main/21-4-2026.jpg)" width="200"></br>
---

## 📌 Project Overview

This project helps you stay ahead in the race to book RCB match tickets by:

- Monitoring the official ticket page
- Detecting "Buy Tickets" buttons
- Alerting you instantly
- Opening the booking page in your logged-in Chrome browser

⚡ Built for speed, simplicity, and real-world usage.

---

## 🚀 Features

- 🔍 Real-time ticket availability tracking
- 🔔 Instant alert (sound + console)
- 🌐 Opens booking page in your real Chrome (logged-in)
- 🔄 Auto-restarts driver on crash
- ⏳ Live countdown between checks
- 🪶 Lightweight and easy to run

---

## 🛠️ Tech Stack

- Python 3.x
- Selenium WebDriver
- Google Chrome

---

## 📂 Project Structure

rcb-ticket-checker/
│<br>
├── RCB_tickets_checker.py   # Main script<br>
└── README.md               # Project documentation<br>

---

## 📦 Installation

### Clone Repository

bash
git clone https://github.com/your-username/rcb-ticket-checker.git<br>

cd rcb-ticket-checker<br>
pip install selenium 

(selenium>=4.15.0)

---

# 📸 Sample Output
When tickets are NOT available:<br>
🕒 16:45:10<br>
❌ Not available yet<br>
⏳ Next check in: 10s

# When tickets ARE available:
🔥 TICKETS AVAILABLE → 'Buy Now'<br>
🔴 Closed debug Chrome.<br>
🌐 Opened in your Chrome — GO BUY NOW!

---

# 🔧 Configuration

## Modify check interval in code:
CHECK_INTERVAL = 10

## Recommended:
10s → Fast detection
20–30s → Safer (less blocking risk)


