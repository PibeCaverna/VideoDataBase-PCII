import mysql.connector
config = {
  "user": "dilfar_user",
  "password": "2024CtrlAltDelete",
  "host": "luca.ar",
  "database": "dilfar_VideoDB-PCII"
}
cnx = mysql.connector.connect(**config)
print ("Conectado: ", cnx.is_connected())
cnx.close()
