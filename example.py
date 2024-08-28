# ejercicio 1
class Dispositivo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

class Telefono(Dispositivo):
    def __init__(self, marca, modelo, numero_telefono):
        super().__init__(marca, modelo)
        self.numero_telefono = numero_telefono

    def llamar(self):
        return f"Llamando al número {self.numero_telefono}"

class Tablet(Dispositivo):
    def __init__(self, marca, modelo, tamano_pantalla):
        super().__init__(marca, modelo)
        self.tamano_pantalla = tamano_pantalla

    def navegar(self):
        return f"Navegando en una pantalla de {self.tamano_pantalla} pulgadas"

class Smartphone(Telefono, Tablet):
    def __init__(self, marca, modelo, numero_telefono, tamano_pantalla):
        self.marca = marca
        self.modelo = modelo
        self.numero_telefono = numero_telefono
        self.tamano_pantalla = tamano_pantalla


miTelefono = Telefono("Samsung", "Galaxy S21", "123-456-789")
miTablet = Tablet("Apple", "iPad Pro", 12.9)
miSmartphone = Smartphone("Google", "Pixel 7", "987-654-321", 6.7)

print(miTelefono.informacion())  
print(miTelefono.llamar())      

print(miTablet.informacion())    
print(miTablet.navegar())       

print(miSmartphone.informacion())  
print(miSmartphone.llamar())      
print(miSmartphone.navegar())     
#punto 2 clase animal y habilidad 

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def describir(self):
        return f"Este pato se llama {self.nombre}"
class Volador:
    def volar(self):
        return " el puede volar"

class Nadador:
    def nadar(self):
        return " y puede nadar"

class Pato(Animal, Volador, Nadador):
    def __init__(self, nombre):
        self.nombre = nombre


miPato = Pato("lucas")   
print(miPato.describir())
print(miPato.volar())
print(miPato.nadar())

#puunto 3 clase instrumentos musicales 

class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre
    def tocar(self):
        return (f"tocando la {self.nombre}")  

class Cuerda:
    def afinar(self):
        return (f"debe afinar la {self.nombre}")

class Percucion:
    def golpear(self):
        return (f"golpeando la {self.nombre} ")

class Guitarra(Instrumento,Cuerda, Percucion):
    def __init__(self, nombre):
        self.nombre = nombre

miGuitarra = Guitarra("guitarrra")
print(f"{miGuitarra.tocar()} {miGuitarra.afinar()} {miGuitarra.golpear()}")   

# clase de Transporte Aéreo y Terrestre

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def mostrarInfo(self):
        return (f"marca: {self.marca}")

class Aereo:
    def volar(self):
        return(f"estoy volando un {self.marca}")

class Terrestre:
    def conducir(self):
        return(f"estoy aterrizando un {self.marca}")

class Helicoptero(Vehiculo, Aereo, Terrestre):
    def __init__(self, marca):
        self.marca = marca

miHelicoptero = Helicoptero("blackhawk")
print(f"{miHelicoptero.mostrarInfo()}, {miHelicoptero.conducir()} ") 
# ejercicio 5
class DispositivosMultimedia:
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        return f"Enciende dispositivo {self.marca}"

class ReproductorAudio(DispositivosMultimedia):
    def __init__(self, marca):
        super().__init__(marca)

    def reproducirAudio(self):
        return f"Reproduciendo audio"
    
    
class ReproductorVideo(DispositivosMultimedia):
    def __init__(self, marca):
        super().__init__(marca)

    def reproducirVideo(self):
        return f"Reproduciendo Video"
class SmartTv(ReproductorAudio, ReproductorVideo):
    def __init__(self, marca):
        self.marca = marca
tv = SmartTv("Samsung")
print(tv.marca)    
print(tv.encender())    
print(tv.reproducirVideo())    
print(tv.reproducirAudio())    

# ejercicio 6

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
    def presentarse(self):
        return f"Hola Guerreros, mi nombre es {self.nombre}"
class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
    def atacar(self):
        return f"Atacando con espada!"
class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
    def lanzarHechizo(self):
        return f"Atacando con magia!"
class Hechicero(Mago, Guerrero):
    def __init__(self, nombre):
        self.nombre = nombre
harry = Hechicero("Harry")
print(harry.presentarse())
print(harry.atacar())
print(harry.lanzarHechizo())