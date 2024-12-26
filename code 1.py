import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Initialize the main application windowz
root = tk.Tk()
root.title("Rental Houses App")
root.geometry("300x600")

# Function to clear the current screen
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# Function to load images
def load_image(image_path, size=(60, 60)):
    img = Image.open("bari_vara\Home_2.jpg")
    img = img.resize(size)
    return ImageTk.PhotoImage(img)

# Page 1 - Welcome Page
def show_welcome_page():
    clear_screen()
    welcome_frame = tk.Frame(root, bg="#D4E2F0")
    welcome_frame.pack(fill="both", expand=True)

    house_icon = tk.Label(welcome_frame, text="🏠", font=("Arial", 50), bg="#D4E2F0")
    house_icon.pack(pady=20)

    welcome_label = tk.Label(welcome_frame, text="Welcome to", font=("Arial", 20, "bold"), bg="#D4E2F0")
    welcome_label.pack(pady=5)

    rental_label = tk.Label(welcome_frame, text="Rental Houses", font=("Arial", 16), fg="red", bg="#D4E2F0")
    rental_label.pack()

    # Load image for the welcome page
    welcome_image = load_image(r"C:\Users\JERIN\OneDrive\Desktop\My Coding\bari_vara\Home_2.jpg", size=(200, 200))
    welcome_image_label = tk.Label(welcome_frame, image=welcome_image, bg="#D4E2F0")
    welcome_image_label.image = welcome_image  # Keep a reference
    welcome_image_label.pack(pady=10)

    next_button = tk.Button(welcome_frame, text="Next", font=("Arial", 14), bg="#00aaff", fg="white", command=show_get_started_page)
    next_button.pack(pady=20)

# Page 2 - Get Started
def show_get_started_page():
    clear_screen()
    start_frame = tk.Frame(root, bg="#ffffff")
    start_frame.pack(fill="both", expand=True)

    # Load image for the get started page
    get_started_image = load_image(r"C:\Users\JERIN\OneDrive\Desktop\My Coding\bari_vara\Home_1.jpg", size=(200, 200))
    get_started_image_label = tk.Label(start_frame, image=get_started_image, bg="#ffffff")
    get_started_image_label.image = get_started_image  # Keep a reference
    get_started_image_label.pack(pady=20)

    text_label = tk.Label(start_frame, text="Let's find your Paradise", font=("Arial", 16), bg="#ffffff", fg="black")
    text_label.pack()

    subtext_label = tk.Label(start_frame, text="Find your perfect dream space with just a few clicks!", font=("Arial", 12), bg="#ffffff", fg="gray", wraplength=250)
    subtext_label.pack(pady=10)

    get_started_button = tk.Button(start_frame, text="Get Started", font=("Arial", 14), bg="#00aaff", fg="white", command=show_login_page)
    get_started_button.pack(pady=20)

# Page 3 - Login/Signup Page
def show_login_page():
    clear_screen()
    login_frame = tk.Frame(root, bg="#E0F7FA")  # Soft blue background
    login_frame.pack(fill="both", expand=True)

    # Load image for the login page
    login_image = load_image(r"C:\Users\JERIN\OneDrive\Desktop\My Coding\bari_vara\Home_3.jpg", size=(200, 200))
    login_image_label = tk.Label(login_frame, image=login_image, bg="#FFD700")
    login_image_label.image = login_image  # Keep a reference
    login_image_label.pack(pady=20)

    login_button = tk.Button(login_frame, text="Log In", font=("Arial", 14), bg="#ffffff", fg="black", command=show_login_form_page)
    login_button.pack(pady=10)

    signup_button = tk.Button(login_frame, text="Sign Up", font=("Arial", 14), bg="#ffffff", fg="black", command=show_signup_page)
    signup_button.pack(pady=10)

# Page - Login Form
def show_login_form_page():
    clear_screen()
    login_form_frame = tk.Frame(root, bg="#E0F7FA")  # Changed background to a light blue
    login_form_frame.pack(fill="both", expand=True)

    title_label = tk.Label(login_form_frame, text="Log In", font=("Arial", 20, "bold"), bg="#E0F7FA")
    title_label.pack(pady=10)

    # Load image for the login form (image 4)
    login_image = load_image(r"C:\Users\JERIN\OneDrive\Desktop\My Coding\bari_vara\Home_4.jpg", size=(200, 200))
    login_image_label = tk.Label(login_form_frame, image=login_image, bg="#E0F7FA")
    login_image_label.image = login_image  # Keep a reference
    login_image_label.pack(pady=20)

    username_label = tk.Label(login_form_frame, text="Username:", bg="#E0F7FA")
    username_label.pack(pady=5)
    username_entry = tk.Entry(login_form_frame)
    username_entry.pack(pady=5)

    password_label = tk.Label(login_form_frame, text="Password:", bg="#E0F7FA")
    password_label.pack(pady=5)
    password_entry = tk.Entry(login_form_frame, show='*')
    password_entry.pack(pady=5)

    login_button = tk.Button(login_form_frame, text="Log In", font=("Arial", 14), bg="#00aaff", fg="white")
    login_button.pack(pady=20)

    back_button = tk.Button(login_form_frame, text="Back", font=("Arial", 14), bg="#00aaff", fg="white", command=show_login_page)
    back_button.pack(pady=10)

# Page - Signup Form
def show_signup_page():
    clear_screen()
    signup_frame = tk.Frame(root, bg="#FFF9C4")  # Light pastel yellow background
    signup_frame.pack(fill="both", expand=True)

    title_label = tk.Label(signup_frame, text="Sign Up", font=("Arial", 20, "bold"), bg="#FFEB3B")
    title_label.pack(pady=10)

    # Load image for the signup form (image 5)
    signup_image = load_image(r"C:\Users\JERIN\OneDrive\Desktop\My Coding\bari_vara\Home_5.jpg", size=(200, 200))
    signup_image_label = tk.Label(signup_frame, image=signup_image, bg="#FFEB3B")
    signup_image_label.image = signup_image  # Keep a reference
    signup_image_label.pack(pady=20)

    username_label = tk.Label(signup_frame, text="Username:", bg="#FFEB3B")
    username_label.pack(pady=5)
    username_entry = tk.Entry(signup_frame)
    username_entry.pack(pady=5)

    email_label = tk.Label(signup_frame, text="Email:", bg="#FFEB3B")
    email_label.pack(pady=5)
    email_entry = tk.Entry(signup_frame)
    email_entry.pack(pady=5)

    password_label = tk.Label(signup_frame, text="Password:", bg="#FFEB3B")
    password_label.pack(pady=5)
    password_entry = tk.Entry(signup_frame, show='*')
    password_entry.pack(pady=5)

    signup_button = tk.Button(signup_frame, text="Sign Up", font=("Arial", 14), bg="#00aaff", fg="white")
    signup_button.pack(pady=20)

    back_button = tk.Button(signup_frame, text="Back", font=("Arial", 14), bg="#00aaff", fg="white", command=show_login_page)
    back_button.pack(pady=10)

# Page - Location List
def show_location_page():
    clear_screen()
    location_frame = tk.Frame(root, bg="#D4E2F0")
    location_frame.pack(fill="both", expand=True)

    title_label = tk.Label(location_frame, text="Location", font=("Arial", 20, "bold"), bg="#D4E2F0")
    title_label.pack(pady=10)

    subtitle_label = tk.Label(location_frame, text="Ashulia model town", font=("Arial", 14), bg="#D4E2F0", fg="gray")
    subtitle_label.pack(pady=5)

    homes = [
        {"name": "Home 1", "image": "home1.png"},
        {"name": "Home 2", "image": "home2.png"},
        {"name": "Home 3", "image": "home3.png"},
        {"name": "Home 4", "image": "home4.png"},
    ]

    for home in homes:
        frame = tk.Frame(location_frame, bg="#D4E2F0")
        frame.pack(pady=10)

        # Load and display the image
        img_photo = load_image(home["image"])
        image_label = tk.Label(frame, image=img_photo, bg="#D4E2F0")
        image_label.image = img_photo  # Keep a reference to avoid garbage collection
        image_label.grid(row=0, column=0, padx=10)

        # Button for each home
        button = tk.Button(frame, text=home["name"], font=("Arial", 14), bg="#ffffff", fg="black", width=10)
        button.grid(row=0, column=1, padx=10)

    back_button = tk.Button(location_frame, text="Back", font=("Arial", 14), bg="#00aaff", fg="white", command=show_login_page)
    back_button.pack(pady=20)

# Start with the Welcome Page
show_welcome_page()

# Run the application
root.mainloop()