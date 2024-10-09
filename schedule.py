import customtkinter as ctk
from tkinter import messagebox
import subprocess
import sys
from PIL import Image, ImageTk


class ScheduleApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Exercise Schedule")
        self.geometry("1600x1600")
        self.selected_days = []

        self.create_widgets()

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text="Exercise Schedule", font=("Helvetica", 24))
        title_label.pack(pady=20)
        

         # Create the top frame (above left and right frames)
        top_frame = ctk.CTkFrame(self, border_width=2, height=100)
        top_frame.pack(side="top", fill="x", padx=20, pady=10)

        # Load and display the gym image
        gym_image = Image.open("img/schedule.jpg")  # Replace with your image path
        gym_image = gym_image.resize((1300, 300))  # Match the window width (800px)
        gym_photo = ImageTk.PhotoImage(gym_image)
        
        image_label = ctk.CTkLabel(top_frame, image=gym_photo, text="")
        image_label.image = gym_photo  # Keep a reference to prevent garbage collection
        image_label.pack(side="left", fill="x", expand=True, padx=20)


        # List of days
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.check_vars = [ctk.BooleanVar(value=False) for _ in self.days]  # Create a list to hold BooleanVars for each checkbox

        # Create a frame for the checkboxes and use grid layout
        checkbox_frame = ctk.CTkFrame(self)
        checkbox_frame.pack(pady=20)

        # Place checkboxes in grid, 3 per row
        for i, (day, var) in enumerate(zip(self.days, self.check_vars)):
            checkbox = ctk.CTkCheckBox(checkbox_frame, text=day, variable=var,fg_color="#C850C0", corner_radius=36)
            checkbox.grid(row=i // 3, column=i % 3, padx=20, pady=10, sticky="w")  # 3 checkboxes per row

        # Submit Button
        submit_button = ctk.CTkButton(self, text="Next", command=self.submit_schedule, corner_radius=10)
        submit_button.pack(pady=20)

    def submit_schedule(self):
        self.selected_days = [day for day, var in zip(self.days, self.check_vars) if var.get()]
        if self.selected_days:
            # Save the selected days to the same line in the text file
            with open("FitnessData.txt", "a") as file:
                file.write("Selected days for exercise: " + ", ".join(self.selected_days) + " |\n")

            print("Selected days for exercise:", self.selected_days)
            messagebox.showinfo("Schedule Submitted", f"You have scheduled exercises on: {', '.join(self.selected_days)}")
            self.open_summary()  # Go to summary screen
        else:
            messagebox.showinfo("Schedule Submitted", "No days selected for exercise.")

    def open_summary(self):
        # Use subprocess to run summary.py
        subprocess.Popen(['python', 'summary.py', ', '.join(self.selected_days)])  # Pass the selected days
        self.quit()  # Close the current app

if __name__ == "__main__":
    app = ScheduleApp()
    app.mainloop()
