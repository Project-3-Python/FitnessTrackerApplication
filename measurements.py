import customtkinter as ctk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk

DATA_FILE = "FitnessData.txt"
ctk.set_appearance_mode("dark")  # Set dark appearance mode

class FitnessApp(ctk.CTk):

    

    def __init__(self):
        super().__init__()
        self.title("Measurements")
        self.geometry("800x1000")

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

        # Create another frame for additional content (Right Frame)
        right_frame = ctk.CTkFrame(middle_frame, fg_color="#a28655", border_color="#8DC6F3", border_width=2, width=150, height=400)
        right_frame.pack(side="right", padx=20, pady=10, fill="both", expand=True)

        # --- Left Frame Content ---
        title_label = ctk.CTkLabel(left_frame, text="Measurements", font=("Helvetica", 24))
        title_label.pack(pady=30)

        # Label for the weight
        weight_label = ctk.CTkLabel(left_frame, text="Enter your weight (kg)", font=("Helvetica", 14))
        weight_label.pack(pady=10)

        # Entry for weight
        self.weight_entry = ctk.CTkEntry(left_frame, placeholder_text="Weight in kg", corner_radius=10, width=300)
        self.weight_entry.pack(pady=10)

        # Label for the height
        height_label = ctk.CTkLabel(left_frame, text="Enter your height (m)", font=("Helvetica", 14))
        height_label.pack(pady=10)

        # Entry for height
        self.height_entry = ctk.CTkEntry(left_frame, placeholder_text="Height in meters", corner_radius=10, width=300)
        self.height_entry.pack(pady=10)

        # --- Right Frame Content (For additional functionality or widgets) ---
        right_label = ctk.CTkLabel(right_frame, text="Additional Information", font=("Helvetica", 24))
        right_label.pack(pady=30)

        # Gender selection
        gender_label = ctk.CTkLabel(right_frame, text="Select your gender", font=("Helvetica", 14))
        gender_label.pack(pady=10)

        self.gender_var = ctk.StringVar(value="Male")  # Default to Male
        male_radio = ctk.CTkRadioButton(right_frame, text="Male", variable=self.gender_var, value="Male", fg_color="#C850C0", corner_radius=36)
        female_radio = ctk.CTkRadioButton(right_frame, text="Female", variable=self.gender_var, value="Female", fg_color="#C850C0", corner_radius=36)
        male_radio.pack(pady=5)
        female_radio.pack(pady=5)

        # Age Entry
        age_label = ctk.CTkLabel(right_frame, text="Enter your age", font=("Helvetica", 14))
        age_label.pack(pady=10)

        self.age_entry = ctk.CTkEntry(right_frame, placeholder_text="Age", corner_radius=10, width=300)
        self.age_entry.pack(pady=10)

        info_label = ctk.CTkLabel(right_frame, text="You can add extra content here.", font=("Helvetica", 14))
        info_label.pack(pady=10)

              # Create the bottom frame (below left and right frames)
        bottom_frame = ctk.CTkFrame(self, fg_color="#FFCC70", border_color="#8DC6F3", border_width=2)
        bottom_frame.pack(side="bottom", fill="x", expand=True, padx=20, pady=10)

        # Continue Button 
        continue_button = ctk.CTkButton(left_frame, text="Continue", command=self.calculate_bmi, corner_radius=10)
        continue_button.pack(side="left", padx=(20, 10), pady=20)

        # Exit Button
        # exit_button = ctk.CTkButton(bottom_frame, text="Exit", command=self.quit, corner_radius=10, fg_color="red")
        # exit_button.pack(side="right", padx=(10, 20), pady=20)

        bottom_label = ctk.CTkLabel(bottom_frame, text="Bottom Frame: Footer or Status", font=("Helvetica", 18))
        bottom_label.pack(pady=10)


    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            self.gender = self.gender_var.get()
            self.age = self.age_entry.get()

            if height <= 0:
                raise ValueError("Height must be greater than 0")

            # Calculate BMI
            bmi = weight / (height ** 2)

            # Categorize the BMI result
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
            elif 25 <= bmi < 30:
                category = "Overweight"
            else:
                category = "Obesity"

            # Save the result to a file in one line
            with open(DATA_FILE, "a") as file:
                file.write(f"Weight: {weight} kg | Height: {height} m | BMI: {bmi:.2f} | Category: {category} | Gender: {self.gender} | Age: {self.age} |")

            # Show the result to the user
            messagebox.showinfo("BMI Result", f"Your BMI is {bmi:.2f} ({category})")

            # Open schedule.py immediately after the message box
            self.open_schedule()

        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")

    def open_schedule(self):
        # Use subprocess to run schedule.py
        subprocess.Popen(['python', 'experience.py'])  # Adjust this line as needed for your environment
        self.quit()  # Close the current app

    

if __name__ == "__main__":
    app = FitnessApp()
    app.mainloop()
 