import tkinter as tk
from tkinter import ttk, messagebox
from model import TennisNaiveBayes

model = TennisNaiveBayes()

def predict():
    o = outlook_var.get()
    t = temp_var.get()
    h = humidity_var.get()
    w = wind_var.get()

    if "" in [o, t, h, w]:
        messagebox.showerror("Error", "Fill all fields!")
        return

    result = model.predict(o, t, h, w)

    if result == "Yes":
        result_label.config(text="Prediction: YES (Play)", fg="green")
    else:
        result_label.config(text="Prediction: NO (Don't Play)", fg="red")

def add_data():
    o = new_outlook_var.get()
    t = new_temp_var.get()
    h = new_humidity_var.get()
    w = new_wind_var.get()
    p = new_play_var.get()

    if "" in [o, t, h, w, p]:
        messagebox.showerror("Error", "Fill all fields!")
        return

    model.add_data(o, t, h, w, p)
    messagebox.showinfo("Success", "New data added!")
    clear_fields()

def clear_fields():
    new_outlook_var.set("")
    new_temp_var.set("")
    new_humidity_var.set("")
    new_wind_var.set("")
    new_play_var.set("")

root = tk.Tk()
root.title("Tennis Naive Bayes Predictor")
root.geometry("450x600")

tk.Label(root, text="Tennis Prediction Model", font=("Arial", 18)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

labels = ["Outlook", "Temperature", "Humidity", "Wind"]
options = [
    ["Sunny", "Overcast", "Rain"],
    ["Hot", "Mild", "Cool"],
    ["High", "Normal"],
    ["Weak", "Strong"]
]

outlook_var = tk.StringVar()
temp_var = tk.StringVar()
humidity_var = tk.StringVar()
wind_var = tk.StringVar()

vars_ = [outlook_var, temp_var, humidity_var, wind_var]

for i in range(4):
    tk.Label(frame, text=labels[i]).grid(row=i, column=0, padx=10, pady=5)
    box = ttk.Combobox(frame, values=options[i], textvariable=vars_[i], state="readonly")
    box.grid(row=i, column=1, padx=10, pady=5)

tk.Button(root, text="Predict", command=predict, bg="blue", fg="white").pack(pady=10)

result_label = tk.Label(root, text="Prediction: ", font=("Arial", 16))
result_label.pack(pady=10)

tk.Label(root, text="Add New Data", font=("Arial", 14)).pack(pady=15)

frame2 = tk.Frame(root)
frame2.pack()

new_outlook_var = tk.StringVar()
new_temp_var = tk.StringVar()
new_humidity_var = tk.StringVar()
new_wind_var = tk.StringVar()
new_play_var = tk.StringVar()

labels2 = ["Outlook", "Temperature", "Humidity", "Wind", "Play (Yes/No)"]
options2 = [
    ["Sunny", "Overcast", "Rain"],
    ["Hot", "Mild", "Cool"],
    ["High", "Normal"],
    ["Weak", "Strong"],
    ["Yes", "No"]
]

vars2 = [new_outlook_var, new_temp_var, new_humidity_var, new_wind_var, new_play_var]

for i in range(5):
    tk.Label(frame2, text=labels2[i]).grid(row=i, column=0, padx=10, pady=5)
    box = ttk.Combobox(frame2, values=options2[i], textvariable=vars2[i], state="readonly")
    box.grid(row=i, column=1, padx=10, pady=5)

tk.Button(root, text="Add Data", command=add_data, bg="green", fg="white").pack(pady=10)

root.mainloop()
