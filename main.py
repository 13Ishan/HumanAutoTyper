import tkinter as tk
from tkinter import scrolledtext, messagebox
import pyautogui
import time
import random
import threading

class AutoTyper:
    def __init__(self, root):
        self.root = root
        self.root.title("Human-Like Auto Typer")
        self.root.geometry("400x500")

        # Text Input
        tk.Label(root, text="Text to Type:").pack(pady=5)
        self.text_input = scrolledtext.ScrolledText(root, width=40, height=10)
        self.text_input.pack(pady=5)

        # WPM Setting
        tk.Label(root, text="Average WPM:").pack()
        self.wpm_val = tk.Entry(root)
        self.wpm_val.insert(0, "60")
        self.wpm_val.pack()

        # Start Button
        self.btn = tk.Button(root, text="START (5s Delay)", command=self.start_typing, bg="green", fg="white")
        self.btn.pack(pady=20)

        tk.Label(root, text="Instructions:\n1. Click Start\n2. Quickly click on your Word/Google Doc\n3. Wait 5 seconds").pack()

    def start_typing(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Empty", "Please paste some text first!")
            return
        
        # Run in background so the app doesn't freeze
        threading.Thread(target=self.logic, args=(text,), daemon=True).start()

    def logic(self, text):
        try:
            wpm = int(self.wpm_val.get())
        except:
            wpm = 60
        
        # 1 word ~ 5 chars. WPM to delay per char:
        delay = 60 / (wpm * 5)

        time.sleep(5) # Give user time to switch windows

        for char in text:
            # Add human "jitter" (randomness)
            variation = random.uniform(-0.02, 0.02)
            final_delay = max(0, delay + variation)
            
            pyautogui.write(char)
            time.sleep(final_delay)

            # Random long break (simulating a "thinking" pause)
            if random.random() < 0.03: # 3% chance per character
                time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoTyper(root)
    root.mainloop()
