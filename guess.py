import tkinter as tk
from tkinter import messagebox
import threading
import time
import os











# Function to handle the guessing logic
def check_guess():
    global countdown_thread
    try:
        guess = int(entry.get())
        if guess == 3:
            messagebox.showinfo("Success", "Congratulations! You guessed the correct number.")
            stop_countdown()  # Stop the shutdown countdown
            root.destroy()  # Close the GUI and stop the program
            os._exit(0)
        else:
            messagebox.showwarning("Try Again", "Wrong guess! Try again.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Function to schedule a shutdown
def schedule_shutdown():
    time.sleep(20)  # Wait for 20 seconds before shutdown
    # os.system("shutdown /s /t 1")  # Uncomment for Windows shutdown
    print("Shutting down...")  # Placeholder for shutdown command

# Function to start the shutdown countdown
def start_countdown():
    global countdown_thread
    countdown_thread = threading.Thread(target=schedule_shutdown)
    countdown_thread.start()

# Function to stop the shutdown countdown
def stop_countdown():
    global countdown_thread
    if countdown_thread.is_alive():
        countdown_thread.join(0)  # Stop the thread
        messagebox.showinfo("Shutdown Cancelled", "Laptop will not shutdown now.")

# GUI Setup
root = tk.Tk()
root.title("Guess the Number")

# Label
label = tk.Label(root, text="Guess the number (1-10):", font=("Arial", 14))
label.pack(pady=10)

# Entry field
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Button
button = tk.Button(root, text="Submit", font=("Arial", 14), command=check_guess)
button.pack(pady=10)

# Start the shutdown countdown when the script runs
start_countdown()

# Run the GUI
root.mainloop()
