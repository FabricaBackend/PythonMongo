# -*- coding: utf-8 -*-
from pymongo import *
from datetime import *
from time import *


print "Conectando al Servidor de Base de Datos Local..."
conexion = MongoClient('localhost',27017) # Conexion local por defecto

#conexion = Connection("usuario:contraseña@servidor.com:27075/basededato") #Conexion a un servidor remoto

#creando/obteniendo un objeto que referencie a la base de datos.
db = conexion['pruebas'] #base de datos a usar

datos_drone = db['datos_drone'] #coleccion con registros de valores del drone

#solicitando los datos de entrada
la_presion = float(raw_input('Ingrese la presion: '))
la_temperatura = float(raw_input('Ingrese la temperatura: '))
la_humedad = float(raw_input('Ingrese la humedad: '))
la_velocidad = float(raw_input('Ingrese la velocidad del viento: '))
numero_estacion = float(raw_input('Ingrese el numero de estacion: '))

fecha = date.today()
fecha_registro = fecha.strftime("%d-%m-%Y")
hora = strftime(" %I:%M %p")

print "Los datos ingresados son:"
print "Presion: " + str(la_presion)
print "Temperatura: " + str(la_temperatura)
print "Humedad: " + str(la_humedad)
print "Velocidad: " + str(la_velocidad)
print "Numero de estacion: " + str(numero_estacion)
print "Fecha: " + fecha_registro
respuesta = raw_input("Estos datos son correctos? (s/n): ")

if respuesta == "s":
#creando el diccionario con los datos del drone
 registro_datos = {"presion": la_presion, "temperatura": la_temperatura, "humedad": la_humedad, "velocidad": la_velocidad, "numeroestacion": numero_estacion, "fecha": fecha_registro + hora}

#insertando los datos en la BD
 datos_drone.insert(registro_datos)
 print('Documento Guardado con EXITO!')

else:
 print "Cancelado!!!"

