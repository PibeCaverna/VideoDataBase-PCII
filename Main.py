import mysql.connector
from utils.kickstart import kickstart
config = {
  "user": "dilfar_Notflix",
  "password": "ZLFyanjnhnvK4v53Whbw",
  "host": "luca.ar",
  "database": "dilfar_Notflix"
}
conexion = mysql.connector.connect(**config)
print ("Conectado: ", conexion.is_connected())
conexion.close()

