import tkinter as tk
from datetime import datetime

LOG_FILE = "keystrokes.log"
logging_enabled = False


def start_logging():
    global logging_enabled
    logging_enabled = True
    status_label.config(text="Status: Logging ON", fg="green")


def stop_logging():
    global logging_enabled
    logging_enabled = False
    status_label.config(text="Status: Logging OFF", fg="red")


def log_key(event):
    if not logging_enabled:
        return

    key = event.keysym
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} - {key}\n")


def main():
    window = tk.Tk()
    window.title("Simple Keylogger (Educational Use Only)")
    window.geometry("450x300")
    window.resizable(False, False)

    title = tk.Label(
        window,
        text="Simple Keystroke Logger",
        font=("Arial", 16, "bold")
    )
    title.pack(pady=10)

    info = tk.Label(
        window,
        text="Keystrokes are logged ONLY while this window is active.\n"
             "User consent is required.",
        font=("Arial", 10),
        justify="center"
    )
    info.pack(pady=5)

    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    start_btn = tk.Button(
        button_frame,
        text="Start Logging",
        width=15,
        command=start_logging
    )
    start_btn.grid(row=0, column=0, padx=10)

    stop_btn = tk.Button(
        button_frame,
        text="Stop Logging",
        width=15,
        command=stop_logging
    )
    stop_btn.grid(row=0, column=1, padx=10)

    global status_label
    status_label = tk.Label(
        window,
        text="Status: Logging OFF",
        font=("Arial", 10),
        fg="red"
    )
    status_label.pack(pady=10)

    typing_area = tk.Label(
        window,
        text="Type here ⬇",
        font=("Arial", 12)
    )
    typing_area.pack()

    window.bind("<KeyPress>", log_key)

    window.mainloop()


if __name__ == "__main__":
    main()