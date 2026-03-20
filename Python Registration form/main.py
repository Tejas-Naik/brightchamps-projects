import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit_form():
    # Get the values from the input fields
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    gender = gender_var.get()
    country = country_var.get()
    bio = bio_text.get("1.0", tk.END).strip()  # Get the text from the text box

    # Validate if all fields are filled
    if not name or not email or not password or not confirm_password or not gender or not country:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Validate if password and confirm password match
    if password != confirm_password:
        messagebox.showerror("Error", "mismatch password.")
        return

    # Display the registration details
    message = f"Name: {name}\nEmail: {email}\nGender: {gender}\nCountry: {country}\nBio: {bio}"
    messagebox.showinfo("Registration Details", message)

    # Clear the input fields after submission
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)
    bio_text.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Set background color
root.configure(bg="#E6E6FA")  # Lavender background color

# Add a custom style to the ttk elements
style = ttk.Style()
style.theme_use("clam")  # You can choose from different themes (classic, clam, default, etc.)
style.configure(
    "TLabel", 
    font=("Helvetica", 12), 
    background="#E6E6FA"
    )  # Lavender background for labels
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TCombobox", font=("Helvetica", 12))

# Create and place labels for each input field
name_label = ttk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

email_label = ttk.Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

password_label = ttk.Label(root, text="Password:")
password_label.grid(
    row=2, 
    column=0, 
    padx=10, 
    pady=5, 
    sticky=tk.W
)

confirm_password_label = ttk.Label(
    root, 
    text="Confirm Password:"
    )
confirm_password_label.grid(
    row=3, 
    column=0, 
    padx=10, 
    pady=5, 
    sticky=tk.W)

gender_label = ttk.Label(root, text="Gender:")
gender_label.grid(
    row=4, 
    column=0, 
    padx=10, 
    pady=5, 
    sticky=tk.W
    )

country_label = ttk.Label(root, text="Country:")
country_label.grid(
    row=5, 
    column=0, 
    padx=10, 
    pady=5, 
    sticky=tk.W
)

bio_label = ttk.Label(root, text="Bio:")
bio_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)

# Create and place input fields for each label
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

email_entry = ttk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

password_entry = ttk.Entry(root, show="*")  # Show asterisks to hide password
password_entry.grid(row=2, column=1, padx=10, pady=5)

confirm_password_entry = ttk.Entry(root, show="*")
confirm_password_entry.grid(row=3, column=1, padx=10, pady=5)

# Create a variable to store the selected gender
gender_var = tk.StringVar()
gender_var.set("Male")  # Default value
male_radio = ttk.Radiobutton(
    root, 
    text="Male", 
    variable=gender_var, 
    value="Male"
)
male_radio.grid(
    row=4, 
    column=1, 
    padx=10, 
    pady=5, 
    sticky=tk.W
)

female_radio = ttk.Radiobutton(
    root, 
    text="Female", 
    variable=gender_var, 
    value="Female"
)
female_radio.grid(
    row=4, 
    column=1, 
    padx=10, 
    pady=5, 
    sticky=tk.W
)

# Create a variable to store the selected country
country_var = tk.StringVar()
country_var.set("India")  # Default value
country_dropdown = ttk.Combobox(
    root, 
    textvariable=country_var, 
    values=[
        "USA", 
        "Canada", 
        "UK", 
        "Australia", 
        "India"
        ]
)
country_dropdown.grid(
    row=5, 
    column=1, 
    padx=10, 
    pady=5, 
    sticky=tk.W
)

# Create a text box for the bio
bio_text = tk.Text(root, width=30, height=5)
bio_text.grid(
    row=6, 
    column=1, 
    padx=10, 
    pady=5
)

# Create and style the submit button
submit_button = ttk.Button(
    root, text="Submit", 
    command=submit_form, 
    cursor="hand2")
submit_button.grid(
    row=7, 
    column=0, 
    columnspan=2, 
    padx=10, 
    pady=10, 
    sticky=tk.W+tk.E
)  # Expand button horizontally

# Set the background and foreground color for the button
submit_button_style = ttk.Style()
submit_button_style.configure(
    "Custom.TButton",
    background="#0066ff",  # 
    foreground="#FFFFFF",  # White text color
    font=("Helvetica", 12),
)
submit_button_style.map(
    "Custom.TButton",
    background=[("active", "#ffab40")],  
    foreground=[("active", "#FFFFFF")],
)
submit_button["style"] = "Custom.TButton"

# Run the main loop
root.mainloop()

