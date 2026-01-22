🔗 📖 Introduction

This project is part of Task-04 and focuses on creating a basic keylogger program for educational purposes.
The goal of this task is to understand how keyboard input events can be captured, processed, and stored in a file using programming concepts—without violating ethical or legal boundaries.
The implemented keylogger captures keystrokes only within the application window and works with explicit user awareness and consent.


🔗 🎯 Objectives

Understand keyboard event handling
Log keystrokes to a file
Apply file handling techniques
Implement timestamps for recorded data
Follow ethical software development practices


🔗 ⚠️ Ethical Considerations
Keylogging can be misused if implemented improperly. Therefore:
❌ No system-wide or background keystroke logging
❌ No hidden or stealth behavior
❌ No data sent externally
✅ Logging occurs only when the application window is active
✅ User is informed clearly when logging is enabled
This project strictly complies with ethical programming standards and is intended only for learning purposes.


🔗 🛠️ Technologies Used
Programming Language: Python 3
GUI Framework: Tkinter (built-in)
File Handling: Python standard I/O
Date & Time: datetime module


🔗 🧩 Program Features
Start and Stop keystroke logging
Visible application window
Logs keys pressed by the user
Stores keystrokes in a text file
Adds timestamps to each key entry


Simple and user-friendly interface
📂 Project Structure
Copy code

Task-04-Simple-Keylogger/
│
├── keylogger.py        # Main program file
├── keystrokes.log     # Output file (auto-generated)
└── README.md          # Project documentation


🔗 ▶️ How the Program Works
The user launches the application.
The GUI window opens with clear instructions.
User clicks Start Logging.
Any key pressed inside the window is recorded.
Keystrokes are saved to keystrokes.log with timestamps.
User can stop logging anytime using Stop Logging.
📄 Output File Description
The program creates a file named:
Copy code

keystrokes.log
Example Output:
Copy code

2026-01-22 15:20:10 - a
2026-01-22 15:20:11 - b
2026-01-22 15:20:12 - Return
Each line contains:
Date
Time
Key pressed


🔗 💻 How to Run the Program
Prerequisites
Python 3.x installed
Steps
Clone or download the project
Open terminal / command prompt
Navigate to the project directory
Run the program:
Copy code
python keylogger.py


🔗 🧠 Learning Outcomes
By completing this task, you will learn:
GUI programming basics
Keyboard event handling
Writing logs to files
Timestamping data
Ethical responsibility in cybersecurity projects


🔗 🚀 Possible Enhancements
Ignore modifier keys (Shift, Ctrl, Alt)
Encrypt log files
Add user authentication
Export logs in CSV format
Implement session-based logging


🔗 📜 Disclaimer
This project is created strictly for educational purposes.
Unauthorized use of keylogging software may be illegal and unethical.
The author is not responsible for misuse of this code.


🔗 ✅ Conclusion
This Task-04 project successfully demonstrates a simple, ethical keylogger that records user keystrokes within a controlled environment. It fulfills all task requirements while respecting privacy, legality, and ethical standards.
