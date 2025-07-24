import tkinter as tk


def increase_count():
  global count
  count += 1
  update_label()


def decrease_count():
  global count
  count -= 1
  update_label()


def update_label():
  label.config(text=f"Count: {count}")


count = 0

window = tk.Tk()
window.title("Counter App")

window.configure(bg='#E6E6FA')

label = tk.Label(text="Count: 0", bg="#E6E6FA",font=("Arial", 20))
label.pack(pady=10)

increase_button = tk.Button(text="Increase", bg="#0066ff",fg="white",command=increase_count)
increase_button.pack(side=tk.LEFT, padx=10,pady=20)

decrease_button = tk.Button(text="Decrease", bg="#ffab40", command=decrease_count)
decrease_button.pack(side=tk.LEFT, padx=10, pady=20)

window.mainloop()

