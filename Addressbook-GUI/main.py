import tkinter as tk
from tkinter import messagebox

def update_listbox():
    contacts_listbox.delete(0, tk.END)
    for contact in contacts:
        contacts_listbox.insert(tk.END, contact['name'])

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    if name and phone and address:
        contact = {'name': name, 'phone': phone, 'address': address}
        contacts.append(contact)
        update_listbox()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Name, phone, and address fields are required.")

def view_details():
    selected_index = contacts_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        contact = contacts[selected_index]
        messagebox.showinfo(
            "Contact Details",
            f"Name: {contact['name']}\nPhone: {contact['phone']}\nAddress: {contact['address']}"
        )

def update_contact():
    selected_index = contacts_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        new_name = name_entry.get()
        new_phone = phone_entry.get()
        new_address = address_entry.get()
        if new_name and new_phone and new_address:
            contacts[selected_index]['name'] = new_name
            contacts[selected_index]['phone'] = new_phone
            contacts[selected_index]['address'] = new_address
            update_listbox()
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Name, phone, and address fields are required.")

def delete_contact():
    selected_index = contacts_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        del contacts[selected_index]
        update_listbox()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Address Book")

contacts = []

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=10)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=10)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=2, column=0, padx=10, pady=10)
address_entry = tk.Entry(root)
address_entry.grid(row=2, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=3, columnspan=2, padx=10, pady=10)

contacts_listbox = tk.Listbox(root)
contacts_listbox.grid(row=4, columnspan=2, padx=10, pady=10)
update_listbox()

view_button = tk.Button(root, text="View Details", command=view_details)
view_button.grid(row=5, column=0, padx=10, pady=10)

update_button = tk.Button(root, text="Update", command=update_contact)
update_button.grid(row=5, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete", command=delete_contact)
delete_button.grid(row=6, columnspan=2, padx=10, pady=10)

root.mainloop()
