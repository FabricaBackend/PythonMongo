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


num_est = float(raw_input("Ingrese el numero de estacion: "))
mostrar = datos_drone.find({"numeroestacion": num_est})
#mostrar = datos_drone.find()
for drone in mostrar:
	#print drone    		
	print "- Presion: %s\n- Temperatura: %s\n- Humedad: %s\n- Velocidad: %s\n- Fecha: %s\n\n" \
      		%(drone['presion'], drone['temperatura'], drone['humedad'], drone['velocidad'], drone['fecha'])
