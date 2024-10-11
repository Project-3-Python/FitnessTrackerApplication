import customtkinter as ctk
from PIL import Image, ImageTk
import subprocess
import time

class SplashScreen:
    def __init__(self, duration=9000):
        self.duration = duration
        self.splash = ctk.CTk()
        self.splash.geometry(f"{self.splash.winfo_screenwidth()}x{self.splash.winfo_screenheight()}")
        self.splash.title("Welcome to Titans Fitness Club")
        self.splash.attributes('-fullscreen', True)

        # Set a background color that matches the logo
        self.splash.configure(fg_color="cyan")  # Dark charcoal color

        # Load and resize logo image
        try:
            logo_image = Image.open("splash2.jpg")
            logo_image = logo_image.resize((300, 300))  # Adjust size as needed
            self.logo_photo = ImageTk.PhotoImage(logo_image)
        except FileNotFoundError:
            print("Logo image not found. Using text instead.")
            self.logo_photo = None

        # Create a frame to center content
        center_frame = ctk.CTkFrame(self.splash, fg_color="transparent")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Add logo
        if self.logo_photo:
            logo_label = ctk.CTkLabel(center_frame, image=self.logo_photo, text="")
            logo_label.pack(pady=(0, 20))

        # Create overlay text with custom font
        self.overlay_label = ctk.CTkLabel(
            center_frame, 
            text="Titans Fitness Club", 
            font=("Helvetica", 40, "bold"), 
            text_color="white"
        )
        self.overlay_label.pack(pady=(0, 20))

        # Add progress bar
        self.progress_bar = ctk.CTkProgressBar(center_frame, width=300)
        self.progress_bar.pack(pady=(0, 20))
        self.progress_bar.set(0)

        # Add version number
        version_label = ctk.CTkLabel(
            self.splash,
            text="Version 1.0",
            font=("Helvetica", 12),
            text_color="white"
        )
        version_label.place(relx=0.95, rely=0.98, anchor="se")

        # Add skip button
        skip_button = ctk.CTkButton(self.splash, text="Skip", command=self.close)
        skip_button.place(relx=0.95, rely=0.05, anchor="ne")

        # Start loading animation
        self.splash.after(100, self.load_animation)

    def load_animation(self):
        steps = 100
        interval = self.duration / steps
        for i in range(steps):
            time.sleep(interval / 1000)  # Convert milliseconds to seconds
            self.progress_bar.set((i + 1) / steps)
            self.splash.update_idletasks()
        self.close()

    def close(self):
        self.splash.destroy()
        try:
            subprocess.Popen(["python", "Login.py"])
        except FileNotFoundError:
            print("Login.py not found. Please check the file name and path.")

    def run(self):
        self.splash.mainloop()

if __name__ == "__main__":
    splash_screen = SplashScreen(duration=9000)
    splash_screen.run()
