from tkinter import *
from tkinter import font
from tkinter import ttk

ventana = Tk()
# Tamaño minimo
ventana.minsize(500, 500)
# Titulo
ventana.title("Proyecto Tkinter")
# No redimensionable
ventana.resizable(0,0)

# Pantallas
def home():
    # Configuramos la pantalla HOME
    homeLabel.config(
        fg="white",
        background="black",
        font=("Arial", 30),
        padx=210,
        pady=20
    )
    # Ubicamos la pantalla HOME
    homeLabel.grid(row=0, column=0)

    # Ubicamos el marco de productos
    productsBox.grid(row=2)

    """
    # Listar productos
    for product in products:
        # Verificamos si se rellenaron los 3 campos
        if len(product) == 3:
            product.append("added")
            Label(productsBox, text=product[0]).grid()
            Label(productsBox, text=product[1]).grid()
            Label(productsBox, text=product[2]).grid()
            Label(productsBox, text="---------------------------").grid()
    """

    for product in products:
        # Verificamos si se rellenaron los 3 campos
        if len(product) == 3:
            product.append("added")
            productsBox.insert("", 0, text=product[0], values=product[1])

    # Ocultar pantallas
    addLabel.grid_remove()
    infoLabel.grid_remove()
    dataLabel.grid_remove()
    addFrame.grid_remove()

def add():
    # Configuramos la pantalla ADD
    addLabel.config(
        fg="white",
        background="black",
        font=("Arial", 30),
        padx=120,
        pady=20
    )
    # Ubicamos la pantalla ADD
    addLabel.grid(row=0, column=0, columnspan=6)
    
    # Ubicamos el marco
    addFrame.grid(row=1)

    # Ubicamos los campos del formulario
    # NOMBRE
    addNameLabel.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    addNameEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    # PRECIO
    addPriceLabel.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    addPriceEntry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    # DESCRIPCION
    addDescLabel.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    addDescEntry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    addDescEntry.config(
        width=30, 
        height=5, 
        font=("Consolas", 12), 
        padx=15, 
        pady=15
    )

    # Separacion
    addSeparator.grid(row=4, column=0)

    # Boton
    boton.grid(row=5, column=1, sticky=NW)
    boton.config(
        padx=15,
        pady=5,
        bg="gray",
        fg="white"
    )

    # Ocultar pantallas
    homeLabel.grid_remove()
    productsBox.grid_remove()
    infoLabel.grid_remove()
    dataLabel.grid_remove()

def info():
    # Configuramos la pantalla INFO
    infoLabel.config(
        fg="white",
        background="black",
        font=("Arial", 30),
        padx=150,
        pady=20
    )
    # Ubicamos las pantalla INFO y DATA
    infoLabel.grid(row=0, column=0)
    dataLabel.grid(row=1, column=0)

    # Ocultar pantalla
    homeLabel.grid_remove()
    productsBox.grid_remove()
    addLabel.grid_remove()
    addFrame.grid_remove()

# Agregar Producto
def addProduct():
    products.append([
        nameData.get(),
        priceData.get(),
        addDescEntry.get("1.0", "end-1c")
    ])

    nameData.set("")
    priceData.set("")
    addDescEntry.delete("1.0", END)

    home()


# Variables
nameData = StringVar()
priceData = StringVar()
products = []

# Campos de pantalla (HOME)
homeLabel = Label(ventana, text="Inicio")

# Tabla de productos
Label(ventana).grid(row=1)
productsBox = ttk.Treeview(height=12, columns=2)
productsBox.grid(row=1, column=0, columnspan=2)
productsBox.heading("#0", text="Producto", anchor=N)
productsBox.heading("#1", text="Precio", anchor=N)

# Campos de pantalla (ADD)
addLabel = Label(ventana, text="Crear producto")

# Marco
addFrame = Frame(ventana)

# Campos del formulario
addNameLabel = Label(addFrame, text="Nombre del producto")
addNameEntry = Entry(addFrame, textvariable=nameData)

addPriceLabel = Label(addFrame, text="Precio del producto")
addPriceEntry = Entry(addFrame, textvariable=priceData)

addDescLabel = Label(addFrame, text="Descripcion del producto")
addDescEntry = Text(addFrame)

# Separador
addSeparator = Label(addFrame)

# Boton
boton = Button(addFrame, text="GUARDAR", command=addProduct)

# Campos de pantalla (INFO y DATA)
infoLabel = Label(ventana, text="Informacion")
dataLabel = Label(ventana, text="Creado por Valenzuela Luciano - 2021")

# Menu superior
menuSuperior = Menu(ventana)
menuSuperior.add_command(label="Inicio", command=home)
menuSuperior.add_command(label="Añadir", command=add)
menuSuperior.add_command(label="Informacion", command=info)
menuSuperior.add_command(label="Salir", command=ventana.quit)

# Cargar menu
ventana.config(menu=menuSuperior)

# Cargar pantalla de inicio
home()

# Cargar ventana
ventana.mainloop()