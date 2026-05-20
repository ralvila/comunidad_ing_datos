#!/usr/bin/env python
# coding: utf-8

# In[25]:


# qué es una función y para qué sirve... 
# Una función es fragmento de código que hará una tarea y podremos utilziar cuantas veces queramos...

def saludar(nombre):
    print(f"Hola, {nombre}")
    
saludar("Ana")


# In[26]:


saludar("Erika")


# In[27]:


#un diccionario agrupa información relacionada bajo una misma variable

persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogotá"
}

print(persona["nombre"])


# In[29]:


nombre1 = "Ana"
edad1 = 25
ciudad1 = "Bogotá"

nombre2 = "Erika"
edad2 = 21
ciudad2 = "Medellín"

nombre3 = "Mari"
edad3 = 28
ciudad3 = "Toronto"

def saludar(nombre, ciudad):
    print(f"Hola, soy, {nombre} y vivo en {ciudad}")


# In[31]:


saludar(nombre1,ciudad1)
saludar(nombre2,ciudad2)
saludar(nombre3,ciudad3)


# In[ ]:


### Datos que se suele manejar en la POO
##color - placa - modelo - año
## Acelera - Frena - reversa...etc

##Datos cuenta bancaria
## titular, saldo, fecha de apertura, estatus, canal apertura...
# Transferir, recibir, retirar

# CONCEPTOS CLAVES:
#Clase - El molde donde llegará la información
#Objeto - Una cosa que crearemos a partir de la clase
#Atributo - Un dato que tendrá el objeto
#Método - La acción que puede hacer el objeto


# In[32]:


#¿Cómo creo una clase?

class Persona:
    pass 


# In[33]:


#¿Cómo crear objetos dentro de una clase?:

persona1 = Persona()
persona2 = Persona()

print(persona1)


# In[42]:


#Vamos a llenar con datos nuestros objetos en la clase Persona

class Persona:
    def __init__(self, nombre, edad):#
        self.nombre = nombre
        self.edad = edad


# In[43]:


persona1 = Persona("Ana",25)
persona2 = Persona("Nicolás",30)

print(persona1.nombre) # Ana
print(persona2.edad) # 30


# In[ ]:


#####Ejercicio 1

#Crear una clase llamará "Producto":
#    - Nombre
#    - Precio
#    - Cantidad en stok
    
#Luego creen 2 productos distintos y los impriman


# In[45]:


# Desarrollo

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
producto1 = Producto ("Manzana", 500, 100)
producto2 = Producto ("Pera", 300, 50)

print(producto1.nombre)
print(producto1.precio)
print(producto1.stock)

print(producto2.nombre)
print(producto2.stock)


# In[46]:


### Método

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")
        
p1 = Persona("Ana",25)
p1.saludar()


# In[47]:


# Métodos que cambian los datos de los objetos:

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")
        
    def cumplir_anio(self):
        self.edad +=1
        print(f"¡Feliz cumpleaños {self.nombre}! ahora tienes {self.edad} años")
        
p1 = Persona("Ana",25)
p1.saludar() #Hola soy Ana y tengo ...
p1.cumplir_anio() #hola soy Ana y tengo {años+1}


# In[48]:


p1.saludar()


# In[ ]:


#EJERCICIO 2

#Toma la clase Producto del ejercicio anterior y agrégale estos métodos:

#1. mostrar_info() → que imprima todos los datos del producto
#2. aplicar_descuento(porcentaje) → que reduzca el precio según el porcentaje dado
#3. vender(cantidad) → que reduzca el stock según la cantidad vendida


# In[ ]:


####  Herencia y polimorfismo ####


# In[3]:


## Estudiante - Nombre - Institución - edad
## Profesor - Nombre - Institución - edad

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")
              
    def presentarse(self):
        print(f"Me llamo {self.nombre}")


# In[4]:


##Clase que va a heredar lo que creamos en Persona

class Estudiante(Persona): ##En paréntesis debe venir la clase padre
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre   #Repetimos lo de la clase persona
        self.edad = edad       #Repetimos lo de la clase persona
        self.carrera = carrera #Nuevo objeto
        
e = Estudiante("Laura",20,"Ingeniería")
e.saludar()
e.presentarse()


# In[5]:


### La función a super() nos ayudará a simplificar código:

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        
e = Estudiante("Laura",20,"Ingeniería")
e.saludar()
e.presentarse()


# In[9]:


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.notas = []
        
    def agregar_nota(self, nota):
        if 0 <= nota <= 5:
            self.notas.append(nota)
            print(f"Nota {nota} registrada")
        else:
            print("Nota inválida")
            
    def promedio(self):
        if not self.notas:
            return 0
        return round(sum(self.notas) / len(self.notas),2)
    
    def mostrar_info(self):
        print(f"\n {self.nombre} | {self.edad} años | {self.carrera}")
        print(f" Notas: {self.notas}")
        print(f" Promedio: {self.promedio()}")

e = Estudiante("Laura",20,"Ingeniería")
e.saludar()
e.presentarse()
e.agregar_nota(4.5)
e.agregar_nota(3.8)
e.mostrar_info()


# In[10]:


####Sobre escribir métodos de la clase padre:

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Soy {self.nombre}")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        
    def presentarse(self):
        print(f"Soy {self.nombre}, estudiante de {self.carrera}")
        
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia
        
    def presentarse(self):
        print(f"Soy {self.nombre}, profesor de {self.materia}")
        
p = Persona("Juan", 35)
e = Estudiante("Laura", 20, "Ingenieria")
pr = Profesor("Carlos", 40, "Matemáticas")

p.presentarse()
e.presentarse()
pr.presentarse()
        


# In[13]:


### Polimorfismos

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hacer_sonidos(self):
        print("...")
        
        
class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")
            
class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")
            
class Vaca(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Muuu!")


# In[14]:


animales = [
    Perro("Firulais"),
    Gato("Michi"),
    Vaca("Lola"),
    Perro("Rex")
]

for animal in animales:
    animal.hacer_sonido()


# In[16]:


####Sistema de pagos

class MetodoPago:
    def __init__(self,titular):
        self.titular = titular
        
    def pagar(self, monto):
        print("Procesando pago...")
        
class Tarjeta(MetodoPago):
    def __init__(self, titular, numero):
        super().__init__(titular)
        self.numero = numero
        
    def pagar(self, monto):
        print(f"Pago de ${monto} en efectivo por {self.titular}")
        
class Efectivo(MetodoPago):
    def pagar(self,monto):
        print(f"Pago de {monto} en efectivo por {self.titular}")
        
class PSE(MetodoPago):
    def __init__(self, titular, banco):
        super().__init__(titular)
        self.banco = banco
        
    def pagar(self, monto):
        print(f"Pago de $ {monto}, via PSE desde {self.banco} por {self.titular}")
              
pagos = [
    Tarjeta("Ana", "123456789"),
    Efectivo("Carlos"),
    PSE("Laura", "Bancolombia")
]
              
              
for pago in pagos:
    pago.pagar(50000)


# In[19]:


#Encapsulación

##sin encapsular

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
cuenta = CuentaBancaria("Ana",1000000)
print(cuenta.saldo)

cuenta.saldo = 9999999999
print(cuenta.saldo)

cuenta.saldo = -500000
print(cuenta.saldo)


# In[20]:


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre #público
        self._edad = edad  #protegido
        
p = Persona("ana",25)
print(p.nombre)
print(p._edad)


# In[30]:


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo # Atributo privado
        
cuenta = CuentaBancaria("ana", 1000000)
#print(cuenta.titular)
print(cuenta.__saldo)


# In[27]:


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
        
    #Método para leer GETTER
    def get_saldo(self):
        return self.__saldo
    
    # Método para modificar de manera controlada será SETTER:
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo <0:
            print("Error: el saldo no puede ser negativo")
        else:
            self.__saldo = nuevo_saldo
            
    def depositar(self, monto):
        if monto >0:
            self.__saldo += monto
            print(f"deposito exitoso. Saldo: ${self.__saldo:,.0f}")
            
    def mostrar_info(self):
        print(f"\n Titular: {self.titular}")
        print(f" saldo: {self.__saldo:,.0f}")
            
            
cuenta = CuentaBancaria("ana",1000000)
cuenta.depositar(50000)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




