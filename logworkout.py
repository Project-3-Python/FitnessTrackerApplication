import customtkinter as ctk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
from datetime import datetime
import sys  # To receive the email from command-line arguments

DATA_FILE = "FitnessTrackerData.txt"
ctk.set_appearance_mode("dark")  # Set dark appearance mode

class FitnessApp(ctk.CTk):
    def __init__(self, email):
        super().__init__()
        self.title("Measurements")
        self.geometry("800x1000")
        self.email = email  # Store the user's email

        # Initialize variables
        self.gender = None
        self.age = None

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
        title_label = ctk.CTkLabel(left_frame, text="Log workouts", font=("Helvetica", 24))
        title_label.pack(pady=20)

        # Label for the workout type
        workout_type_label = ctk.CTkLabel(left_frame, text="Select type of workout", font=("Helvetica", 14))
        workout_type_label.pack(pady=5)

        # Dropdown for workout types
        self.workout_type_var = ctk.StringVar(value="Select Workout Type")
        self.workout_type_dropdown = ctk.CTkComboBox(left_frame, variable=self.workout_type_var, values=["Plank", "Squat", "Lunge", "Wall sit", "Arm circles", "Push-up", "Step up", "Shoulder bridge", "Tuck jump", "Mountain climber", "Stair climb with bicep curl", "Deadlifts", "Leg press", "Pull up", "Bench press"])
        self.workout_type_dropdown.pack(pady=5)

        # Label for the duration
        duration_label = ctk.CTkLabel(left_frame, text="Enter duration (m)", font=("Helvetica", 14))
        duration_label.pack(pady=5)

        # Entry for duration
        self.duration_entry = ctk.CTkEntry(left_frame, placeholder_text="Duration in minutes", corner_radius=10, width=300)
        self.duration_entry.pack(pady=10)

        # Create a frame for the buttons
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(side="top", fill="x", padx=20, pady=(10, 20))

        # Save Button 
        save_button = ctk.CTkButton(button_frame, text="Save", corner_radius=10, command=self.save_workout)
        save_button.pack(pady=(10, 5))  # Add some padding for spacing

        # Dashboard Button 
        dashboard_button = ctk.CTkButton(button_frame, text="Go to dashboard", command=self.open_dashboard, corner_radius=10)
        dashboard_button.pack(pady=(5, 10))  # Add some padding for spacing

    def save_workout(self):
        # Get current date
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        workout_type = self.workout_type_var.get()
        duration = self.duration_entry.get()

        # Validate input
        if workout_type == "Select Workout Type" or not duration.isdigit():
            messagebox.showerror("Input Error", "Please select a workout type and enter a valid duration.")
            return

        # Save the data to the text file, along with the user's email
        with open(DATA_FILE, "a") as file:
            file.write(f"{self.email}, {current_date}, {workout_type}, {duration} minutes\n")

        # Clear the entry after saving
        self.duration_entry.delete(0, 'end')
        self.workout_type_var.set("Select Workout Type")
        messagebox.showinfo("Success", "Workout data saved successfully!")

    def open_dashboard(self):
        # Use subprocess to run dashboard.py and pass the user's email
        subprocess.Popen(['python', 'dashboard.py', self.email])  # Pass the user's email to dashboard
        self.quit()  # Close the current app

if __name__ == "__main__":
    # Get the email passed from login.py
    user_email = sys.argv[1]  # Retrieve the email from command-line arguments
    app = FitnessApp(user_email)
    app.mainloop()
