# security-project

# USB Security Tool (Cyberpunk GUI)

## 📌 Overview

This project is a **USB Port Security Application** built using Python.
It provides a cyberpunk-themed graphical interface to **enable or disable USB storage devices** on a Windows system.

---

## ⚙️ Features

* 🔐 Login system (basic authentication)
* 💻 Cyberpunk-themed GUI
* 🔌 Enable / Disable USB storage devices
* 🖼️ Dynamic background UI
* 🧠 Simple and extensible codebase

---

## 🖥️ System Requirements

* OS: **Windows (Required)**
* Python: **3.8+**
* Administrator privileges (important for USB control)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/usb-security-tool.git
cd usb-security-tool
```

---

### 2. Create virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it:

**Windows:**

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing:

```bash
pip install customtkinter pillow
```

---

## ▶️ Running the Application

```bash
python main.py
```

---

## 🔑 Default Login

```text
Username: admin
Password: 1234
```

---

## ⚠️ Important Notes

* Must run **as Administrator** for USB control to work
* Only **USB storage devices** (pendrives, external HDDs) are blocked
* Keyboard, mouse, and other USB devices will still work

---

## 📁 Project Structure

```text
usb-security-tool/
│
├── main.py              # Main GUI + Login
├── usb_control.py       # USB enable/disable logic
├── cyberpunk_bg.jpg     # Background image
├── requirements.txt     # Dependencies
```

---

## 🧠 How It Works

* Uses Windows Registry (`USBSTOR`) to control USB storage access
* GUI built with CustomTkinter
* Background + animations handled via Canvas

---

## 🛠️ For Developers (Team Members)

### Modify UI

* Edit `main.py` for GUI changes

### Modify USB logic

* Edit `usb_control.py`

### Add features (suggested)

* Database login system
* USB monitoring
* Device whitelist
* Logging system

---

## 🚀 Future Improvements

* Real-time USB detection
* Role-based access control
* Intruder detection (webcam)
* Advanced cyberpunk animations

---

## 🧪 Troubleshooting

### Module not found

```bash
pip install customtkinter pillow
```

### USB not disabling

* Ensure app is run as **Administrator**

---

## 👥 Team Notes

* Use branches for new features
* Test before pushing changes
* Keep commits clean and descriptive

---

## 📄 License

This project is for educational purposes.
