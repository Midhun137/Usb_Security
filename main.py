import customtkinter as ctk
from tkinter import messagebox, Canvas
from PIL import Image, ImageTk
import random
import cv2
import time
from datetime import datetime
import os

from usb_control import disable_usb, enable_usb

ctk.set_appearance_mode("dark")

# ---------------- INTRUDER CAPTURE ----------------
def capture_intruder():
    try:
        cam = cv2.VideoCapture(0)

        if not cam.isOpened():
            print("❌ Camera not accessible")
            return

        time.sleep(2)  # allow camera to start

        ret, frame = cam.read()

        if ret:
            if not os.path.exists("intruders"):
                os.makedirs("intruders")

            filename = f"intruders/intruder_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            cv2.imwrite(filename, frame)

            print("✅ Intruder captured:", filename)
        else:
            print("❌ Failed to capture image")

        cam.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print("ERROR:", e)

# ---------------- BACKGROUND ----------------
class ResizableBackground:
    def __init__(self, canvas, path):
        self.canvas = canvas
        self.image = Image.open(path)
        self.bg = None
        self.canvas.bind("<Configure>", self.resize)

    def resize(self, event):
        resized = self.image.resize((event.width, event.height))
        self.bg = ImageTk.PhotoImage(resized)
        self.canvas.delete("bg")
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw", tags="bg")

# ---------------- SNOW EFFECT ----------------
class SnowEffect:
    def __init__(self, canvas):
        self.canvas = canvas
        self.particles = []

        for _ in range(80):
            x = random.randint(0, 800)
            y = random.randint(0, 600)
            size = random.randint(2, 4)
            speed = random.uniform(1, 3)

            p = {
                "id": canvas.create_oval(x, y, x+size, y+size,
                                         fill="#00FFFF",
                                         outline="",
                                         tags="snow"),
                "speed": speed
            }
            self.particles.append(p)

        self.animate()

    def animate(self):
        for p in self.particles:
            self.canvas.move(p["id"], 0, p["speed"])
            pos = self.canvas.coords(p["id"])

            if pos[1] > self.canvas.winfo_height():
                x = random.randint(0, self.canvas.winfo_width())
                self.canvas.coords(p["id"], x, 0, x+3, 3)

        self.canvas.tag_raise("snow")
        self.canvas.after(30, self.animate)

# ---------------- LOGIN WINDOW ----------------
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CYBER LOGIN")
        self.root.geometry("800x600")

        canvas = Canvas(root, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        ResizableBackground(canvas, "city.jpg")

        canvas.create_rectangle(0, 0, 2000, 2000,
                                fill="#000000",
                                stipple="gray25")

        SnowEffect(canvas)

        frame = ctk.CTkFrame(root,
                             width=320,
                             height=360,
                             fg_color="#0a0a0a",
                             corner_radius=25,
                             border_width=2,
                             border_color="#00FFFF")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(frame,
                     text="ACCESS TERMINAL",
                     text_color="#00FFFF",
                     font=("Consolas", 18, "bold")).pack(pady=20)

        self.username = ctk.CTkEntry(frame, placeholder_text="Username")
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(frame, placeholder_text="Password", show="*")
        self.password.pack(pady=10)

        ctk.CTkButton(frame,
                      text="LOGIN",
                      fg_color="#FF00FF",
                      command=self.login).pack(pady=20)

    def login(self):
        if self.username.get() == "admin" and self.password.get() == "1234":
            self.root.destroy()
            main_app()
            capture_intruder()
            print("✅ Access granted")
        else:
            print("❗ Wrong login detected")
            capture_intruder()
            messagebox.showerror("ERROR", "ACCESS DENIED")

# ---------------- MAIN WINDOW ----------------
def main_app():
    app = ctk.CTk()
    app.title("USB CONTROL")
    app.geometry("800x600")

    canvas = Canvas(app, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    ResizableBackground(canvas, "city.jpg")

    canvas.create_rectangle(0, 0, 2000, 2000,
                            fill="#000000",
                            stipple="gray25")

    SnowEffect(canvas)

    frame = ctk.CTkFrame(app,
                         width=320,
                         height=360,
                         fg_color="#0a0a0a",
                         corner_radius=25,
                         border_width=2,
                         border_color="#00FFFF")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    ctk.CTkLabel(frame,
                 text="USB CONTROL PANEL",
                 text_color="#00FFFF",
                 font=("Consolas", 18, "bold")).pack(pady=20)

    def disable_action():
        if disable_usb():
            messagebox.showinfo("SYSTEM", "USB DISABLED")
        else:
            messagebox.showerror("ERROR", "FAILED")

    def enable_action():
        if enable_usb():
            messagebox.showinfo("SYSTEM", "USB ENABLED")
        else:
            messagebox.showerror("ERROR", "FAILED")

    ctk.CTkButton(frame,
                  text="DISABLE USB",
                  fg_color="#FF0040",
                  command=disable_action).pack(pady=10)

    ctk.CTkButton(frame,
                  text="ENABLE USB",
                  fg_color="#00FFAA",
                  command=enable_action).pack(pady=10)

    app.mainloop()

# ---------------- START ----------------
root = ctk.CTk()
LoginApp(root)
root.mainloop()