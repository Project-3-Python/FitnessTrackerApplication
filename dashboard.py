import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import os

DATA_FILE = "FitnessTrackerData.txt"  # Assuming this is the file where workouts are saved
ctk.set_appearance_mode("dark")  # Set dark appearance mode

class FitnessApp(ctk.CTk):
    def __init__(self, email):
        super().__init__()
        self.title("Dashboard")
        self.geometry("800x1000")
        self.email = email  # Store the user's email for filtering the history

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Create the top frame (above left and right frames)
        top_frame = ctk.CTkFrame(self, border_width=2, height=100)
        top_frame.pack(side="top", fill="x", padx=20, pady=10)

        # Load and display the gym image
        gym_image = Image.open("img/gym.jpg")  # Replace with your image path
        gym_image = gym_image.resize((800, 300))  # Match the window width (800px)
        gym_photo = ImageTk.PhotoImage(gym_image)

        image_label = ctk.CTkLabel(top_frame, image=gym_photo, text="")
        image_label.image = gym_photo  # Keep a reference to prevent garbage collection
        image_label.pack(side="left", fill="x", expand=True, padx=20)

        # Create a frame for the main section (Middle Frame to hold left and right frames)
        middle_frame = ctk.CTkFrame(self)
        middle_frame.pack(side="top", fill="both", expand=True, padx=20, pady=10)

        # Create a frame for the left section (Left Frame)
        left_frame = ctk.CTkFrame(middle_frame, fg_color="#a28655", border_color="#8DC6F3", border_width=2, width=150, height=400)
        left_frame.pack(side="left", padx=20, pady=10, fill="both", expand=True)

        # --- Left Frame Content ---
        title_label = ctk.CTkLabel(left_frame, text="Dashboard", font=("Helvetica", 30))
        title_label.pack(pady=50)

        # View History Button 
        view_history_button = ctk.CTkButton(left_frame, text="View History", corner_radius=10, command=self.view_history)
        view_history_button.pack(pady=(10, 10))  # Add some padding for spacing

        # Log Workout Button 
        logworkout_button = ctk.CTkButton(left_frame, text="Log Workouts", corner_radius=10, command=self.log_workout)
        logworkout_button.pack(pady=(10, 10))  # Add some padding for spacing

        # View Progress Button 
        view_progress_button = ctk.CTkButton(left_frame, text="View Progress", command=self.view_progress, corner_radius=10)
        view_progress_button.pack(pady=(5, 10))  # Add some padding for spacing

        # Textbox to display workout history
        self.history_textbox = ctk.CTkTextbox(middle_frame, height=400, width=600)
        self.history_textbox.pack(pady=20)

    def view_history(self):
        """View the user's workout history filtered by email."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                history_lines = file.readlines()

            user_history = [line for line in history_lines if line.startswith(self.email)]

            # Clear the text box before displaying new content
            self.history_textbox.delete('1.0', 'end')

            if user_history:
                # Display the user's workout history in the textbox
                for entry in user_history:
                    self.history_textbox.insert('end', entry + '\n')
            else:
                self.history_textbox.insert('end', "No workout history found for your account.")
        else:
            messagebox.showerror("File Not Found", f"{DATA_FILE} not found. No history available.")

    def log_workout(self):
        # Use subprocess to run logworkout.py
        subprocess.Popen(['python', 'logworkout.py', self.email])  # Pass the user's email to logworkout
        self.quit()  # Close the current app

    def view_progress(self):
        # Functionality to view progress can be implemented here, if needed
        pass

if __name__ == "__main__":
    import sys
    user_email = sys.argv[1]  # Retrieve the user's email from command-line arguments
    app = FitnessApp(user_email)
    app.mainloop()
