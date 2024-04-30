import tkinter as tk
def display_text():
    entered_text= text_entry.get()
    label.config(text=entered_text)
root= tk.Tk()
root.title("metin görüntüleyici")

text_entry = tk.Entry(root, width=20)
text_entry.pack(pady=10)

button= tk.Button(root, text="göster",command=display_text)
button.pack(pady=5)

label= tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()