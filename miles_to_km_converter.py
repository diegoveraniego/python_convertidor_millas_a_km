from tkinter import *

window = Tk()
window.title("Convertidor de Millas a Km")
window.minsize(width=300, height=150)
window.config(padx=40, pady=40)

def convert_miles_to_km():
    miles = mile_input.get()
    km = float(miles) * 1.60939
    rounded_km = round(km, 2)
    km_value.config(text=str(rounded_km))

convert_text = Label(text="es igual a", font=("Arial", 12, "normal"))
convert_text.grid(column=0, row=1)

mile_input = Entry(width=10)
mile_input.insert(END, string="0")
mile_input.grid(column=2, row=0)


km_value = Label(text="0")
km_value.grid(column=2 ,row=1)

convert_button = Button(text="Calcular", command=convert_miles_to_km)
convert_button.grid(column=2, row=2)

miles_label = Label(text="Millas")
miles_label.grid(column=3, row=0)
kms_label = Label(text="Km")
kms_label.grid(column=3, row=1)

window.mainloop()