import customtkinter as ctk
import sys

class SummaryApp(ctk.CTk):
    def __init__(self, selected_days):
        super().__init__()
        self.title("Summary")
        self.geometry("400x400")

        # Title Label
        title_label = ctk.CTkLabel(self, text="Summary ", font=("Helvetica", 18))
        title_label.pack(pady=10)

        # Load the last entry from the text file
        last_entry = self.get_last_entry("FitnessData.txt")

        # Display the last fitness data entry
        fitness_display = ctk.CTkLabel(self, text=last_entry, font=("Helvetica", 14), wraplength=300)
        fitness_display.pack(pady=10)

        # Display the exercise schedule
        # schedule_label = ctk.CTkLabel(self, text="Scheduled Exercise Days", font=("Helvetica", 14))
        # schedule_label.pack(pady=10)

        # Display the selected exercise days (if provided)
        # schedule_display = ctk.CTkLabel(self, text=selected_days if selected_days else "No days selected.", font=("Helvetica", 14))
        # schedule_display.pack(pady=10)

        # Add a close button for the summary window
        close_button = ctk.CTkButton(self, text="Close", command=self.quit, corner_radius=10)
        close_button.pack(pady=10)

        #Proceed to workout button
         # Add a close button for the summary window
        workout_button = ctk.CTkButton(self, text="Start workout", corner_radius=10)
        workout_button.pack(pady=10)

    def get_last_entry(self, file_path):
        """Read the last non-empty entry from the text file."""
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                
                # Return the last non-empty line
                for line in reversed(lines):
                    if line.strip():  # Skip empty lines
                        return line.strip()  # Return the last non-empty line
                return "No data found."
        except FileNotFoundError:
            return "No data found."

if __name__ == "__main__":
    # Extract the schedule days passed from schedule.py
    if len(sys.argv) > 1:
        selected_days = sys.argv[1]
    

    app = SummaryApp(selected_days)
    app.mainloop()
