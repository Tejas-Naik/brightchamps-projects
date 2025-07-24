import tkinter as tk

def is_valid_number(value):
    return value.replace('.', '', 1).isdigit()

def convert_weight():
    weight = entry_weight.get()
    selected_unit = unit_choices.get()
    result_text.set("")

    if not weight or not is_valid_number(weight):
        result_text.set("Invalid input. Please enter a valid number.")
        return

    weight = float(weight)

    if selected_unit == "Kilograms to Pounds":
        result = weight * 2.20462
        result_text.set(f"{weight:.2f} kilograms is equal to {result:.2f} pounds.")
    elif selected_unit == "Pounds to Kilograms":
        result = weight / 2.20462
        result_text.set(f"{weight:.2f} pounds is equal to {result:.2f} kilograms.")
    elif selected_unit == "Kilograms to Ounces":
        result = weight * 35.274
        result_text.set(f"{weight:.2f} kilograms is equal to {result:.2f} ounces.")
    elif selected_unit == "Ounces to Kilograms":
        result = weight / 35.274
        result_text.set(f"{weight:.2f} ounces is equal to {result:.2f} kilograms.")
    else:
        result_text.set("Invalid conversion selected.")

# Create the main application window
app = tk.Tk()
app.title("Weight Conversion App")
app.geometry("400x250")

# Styling
app.configure(bg="#C5DFF8")  # Set background color for the main window

label_weight = tk.Label(app, text="Enter Weight:", bg="#C5DFF8",font=("Helvetica", 14))
label_weight.pack(pady="5", anchor="center")

entry_weight = tk.Entry(app, bg="white", font=("Arial", 12))
entry_weight.pack(pady="5", anchor="center")

unit_choices = tk.StringVar(app)
unit_choices.set("Kilograms to Pounds")

unit_options = ["Kilograms to Pounds", "Pounds to Kilograms", "Kilograms to Ounces", "Ounces to Kilograms"]

unit_menu = tk.OptionMenu(app, unit_choices, *unit_options)
unit_menu.config(bg="white", font=("Arial", 12))
unit_menu.pack(pady="5", anchor="center")

btn_convert = tk.Button(app, text="Convert", command=convert_weight, bg="#0066ff", fg="white", font=("Arial", 12))
btn_convert.pack(pady="5", anchor="center")

result_text = tk.StringVar()
label_result = tk.Label(app, textvariable=result_text, bg="#C5DFF8",font=("Helvetica", 12))
label_result.pack(pady="5", anchor="center")

# Run the main event loop

app.mainloop()

