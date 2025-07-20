from tkinter import *

def button_clicked():
    print("Me apretaron")
    my_label.config(text="El botón fue apretado")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("Mi primer programa con GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label

my_label = Label(text="Soy una etiqueta", font=("Arial", 15,  "bold"))
my_label.config(text="Texto nuevo") # Nos permite cambiar las propiedades
my_label.grid(column=0, row=0)

# Button

button = Button(text="Apretame", command=button_clicked) #without ()
#button.pack()
button.grid(column=1, row=1)

# New Button

new_button = Button(text="Botón Nuevo", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry

input = Entry(width=10)  # Si quiero tomar control del value, debo usar get
input.grid(column=3, row=2)

window.mainloop()