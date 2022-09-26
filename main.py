


pages = [
    "Page 0) Gracias por ingresar a nustra página,\n A continuación te brindaremos nuestros servicio y precios \nQué vas a hacer?\n1) Crear Página web para mi compañía\n2) Servicio de Marketing Digital\n3) Búsqueda de Personal IT",
    "Page 1) Tu página comienza web en $100.000\n 3 $100.000 Servicio Básico \n $120.000 5 páginas \n $150.000 5 páginas y base de datos  \n Gracias escribinos por email",
    "Page 2) El servicio de Marketing digital tiene el siguiente costo \n $20.000 1 red social por mes \n $30.000 2 redes sociales por mes \n $50.000 4 redes sociales por mes \n los contratos se celebran por 6 meses mínimos  \n Gracias escribinos por email", 
    "Page 3) Búsqueda de personal IT  \n 1) tu primer búsqueda el costo es el 70% del primer sueldo bruto... \n 2) Tus dos primeras búsquedas 60% del costo del sueldo bruto... \n 3) consultar otras posibilidades\n Gracias escribinos por email" ,
    
]

def showPage(pageNumber):
    text = pages[pageNumber]
    print(text)
    response = input()
    showPage(int(response))

showPage(0)