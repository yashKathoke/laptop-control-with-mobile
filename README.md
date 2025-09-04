# Web-Based Remote Mouse & Keyboard Controller

A simple **remote control app** that allows you to control your laptop's mouse and keyboard using your phone over Wi-Fi. Works entirely via a web browser — no installation required on the phone.

---

## Features

* **One-finger drag:** Move the mouse.
* **Tap on touchpad:** Left click.
* **Two-finger tap:** Right click.
* **Two-finger swipe:** Scroll.
* **Keyboard input:** Supports letters, numbers, Enter, Backspace, Arrows, and more.
* **Connect/Disconnect button** for easy connection management.
* **Techy "hacker movie" UI** with neon-green terminal-style design.

---

## Requirements

* Python 3.10+
* Libraries in `requirements.txt`:

```txt
websockets==11.0.3
pynput==1.7.6
```

* Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Installation & Usage

1. **Clone the repository:**

```bash
git clone https://github.com/yashKathoke/laptop-control-with-mobile.git
cd laptop-control-with-mobile
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the server:**

```bash
python server.py
```

4. **Connect from your phone:**

* The server will print a URL in the console, for example:

```
Remote Control Started 🚀
Open this on your phone: http://192.168.1.100:8000
```

* Open this URL in your mobile browser while connected to the same Wi-Fi (or hotspot).

5. **Use the remote control:**

* Drag on the touchpad area to move the mouse.
* Tap or two-finger tap for left/right click.
* Two-finger swipe to scroll.
* Type in the keyboard input box to send text or special keys.

---

## File Structure

```
.
├── server.py          # Python WebSocket & HTTP server
├── requirements.txt   # Python dependencies
├── README.md
└── static
    └── index.html     # Web-based touchpad & keyboard UI
```

---

## Notes / Tips


* **IP Address:** If the server prints `127.0.0.1`, replace it with your laptop's local network IP.
* **Performance:** Use a fast Wi-Fi network for smooth mouse movements.
* **Disconnecting:** Use the Connect/Disconnect button in the UI to safely close the WebSocket.

---