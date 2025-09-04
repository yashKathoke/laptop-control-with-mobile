import asyncio
import websockets
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key
import http.server
import socketserver
import threading
import os
import socket

mouse = MouseController()
keyboard = KeyboardController()

# --- WebSocket Handler ---
async def handler(websocket):
    async for message in websocket:
        try:
            parts = message.split(":")
            if parts[0] == "move":
                dx, dy = float(parts[1]), float(parts[2])
                mouse.move(dx, dy)

            elif parts[0] == "click":
                if parts[1] == "left":
                    mouse.click(Button.left, 1)
                elif parts[1] == "right":
                    mouse.click(Button.right, 1)

            elif parts[0] == "scroll":
                dx, dy = float(parts[1]), float(parts[2])
                mouse.scroll(dx, dy)

            elif parts[0] == "text":
                text = message[5:]  # remove "text:"
                keyboard.type(text)

            elif parts[0] == "key":
                key = parts[1]
                special_keys = {
                    "Enter": Key.enter,
                    "Backspace": Key.backspace,
                    "Tab": Key.tab,
                    "Escape": Key.esc,
                    "ArrowUp": Key.up,
                    "ArrowDown": Key.down,
                    "ArrowLeft": Key.left,
                    "ArrowRight": Key.right,
                    "Shift": Key.shift,
                    "Control": Key.ctrl,
                    "Alt": Key.alt,
                }
                if key in special_keys:
                    keyboard.press(special_keys[key])
                    keyboard.release(special_keys[key])

        except Exception as e:
            print(f"⚠️ Error handling message '{message}': {e}")

# --- Run WebSocket server ---
async def websocket_server():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

# --- HTTP server for index.html ---
def http_server():
    os.chdir("static")  # serve from static folder
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", 8000), handler) as httpd:
        httpd.serve_forever()

# --- Helper: Get local IP ---
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

# --- Main ---
if __name__ == "__main__":
    ip = get_local_ip()
    url = f"http://{ip}:8000"
    print("===================================")
    print(" Remote Control Started 🚀")
    print(f" Open this on your phone: {url}")
    print("===================================")

    threading.Thread(target=http_server, daemon=True).start()
    asyncio.run(websocket_server())
