import customtkinter as ctk
import tkinter.messagebox as tkmb
import re  # For email validation

# Set the appearance mode and default color theme
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

# Create the main app window
app = ctk.CTk()
app.title("Titans Fitness Club - Login")

# Get the screen width and height
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Set the geometry to 80% of the screen size
window_width = int(screen_width * 0.6)
window_height = int(screen_height * 0.6)
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
app.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Optional: Set fullscreen
app.attributes('-fullscreen', True)

# Create a main frame to hold all widgets with a matching background
main_frame = ctk.CTkFrame(app, fg_color="cyan")  # Match splash screen color
main_frame.pack(expand=True, fill="both", padx=40, pady=40)

# Function to get user data from the file
def get_user_data():
    user_data = {}
    try:
        with open("FitnessTrackerData.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) == 3:
                    name = parts[0].split(": ")[1]
                    email = parts[1].split(": ")[1]
                    password = parts[2].split(": ")[1]
                    user_data[email] = {"name": name, "password": password}
    except FileNotFoundError:
        print("FitnessTrackerData.txt not found. No user data available.")
    return user_data

# Function to validate email format
def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

# Updated login function
def login():
    email = username_entry.get()
    password = password_entry.get()
    
    # Load the user data from the file
    users = get_user_data()

    # Check if the email exists and password matches
    if email in users and users[email]["password"] == password:
        tkmb.showinfo(title="Login Successful", message=f"Welcome {users[email]['name']}!")
    else:
        tkmb.showerror(title="Login Failed", message="Invalid username or password")

# Function to open the registration window
def open_registration_window():
    import Register  # Import the Register module
    Register.open_registration_window(app)  # Call the function from Register.py

# Label for the app title
label = ctk.CTkLabel(main_frame, text="Titans Fitness Club - Login", font=("Helvetica", 24, "bold"), text_color="white")
label.pack(pady=20)

# Email entry
username_entry = ctk.CTkEntry(main_frame, placeholder_text="Username(email)", width=300)
username_entry.pack(pady=12)

# Password entry
password_entry = ctk.CTkEntry(main_frame, placeholder_text="Password", show="*", width=300)
password_entry.pack(pady=12)

# Login button
login_button = ctk.CTkButton(main_frame, text="Login", command=login, width=300)
login_button.pack(pady=12)

# Forgot password label
forgot_password = ctk.CTkLabel(main_frame, text="Forgot Password?", cursor="hand2", text_color="purple")
forgot_password.pack(pady=12)

# Register label
register_label = ctk.CTkLabel(main_frame, text="Don't have an account? Register here", cursor="hand2", text_color="purple")
register_label.pack(pady=12)
register_label.bind("<Button-1>", lambda e: open_registration_window())

# Start the application
app.mainloop()
