# 🎟️ RCB-Ticket-Checker
A lightweight Python tool to monitor the official RCB ticket website.
Continuously checks for ticket availability in real time. Detects “Buy Tickets” & alerts you instantly.
Allows you to customize the checking interval and alerts you immediately when tickets are available.

---

## 📌 Project Overview

This project helps you stay ahead in the race to book RCB match tickets by:

- Monitoring the official ticket page
- Detecting "Buy Tickets" buttons
- Alerting you instantly by opening the tickets page & sound alert

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
git clone https://github.com/chetanmauth/RCB-Ticket-Checker.git<br>

cd rcb-ticket-checker<br>
pip install selenium 

(selenium>=4.15.0)

---

## 📸 Sample Output
### When tickets are NOT available:<br>
🕒 16:45:10<br>
❌ Not available yet<br>
⏳ Next check in: 10s

### When tickets ARE available:
🔥 TICKETS AVAILABLE → 'Buy Now'<br>
🔴 Closed debug Chrome.<br>
🌐 Opened in your Chrome — GO BUY NOW!


## Sucessfully Triggered & Booked Ticket

<img src="https://github.com/chetanmauth/RCB-Ticket-Checker/blob/main/21-4-2026.jpg" width="300"></br>

---

## 🔧 Configuration

### Modify check interval in code:
CHECK_INTERVAL = 10

## Recommended:
10s → Fast detection
20–30s → Safer (less blocking risk)


