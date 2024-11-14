import mysql.connector

config = {
  "user": "dilfar_user",
  "password": "2024CtrlAltDelete",
  "host": "luca.ar",
  "database": "dilfar_VideoDB-PCII"
}

cnx = mysql.connector.connect(**config)
print ("Conectado: ", cnx.is_connected())

Creatabla = """
    CREATE TABLE Usuarios(
        id_usuario INTEGER PRIMARY KEY AUTO_INCREMENT,
        e_mail VARCHAR(40) NOT NULL,
        contraseña VARCHAR(40) NOT NULL)
    """
with cnx.cursor() as consulta:
    consulta.execute(Creatabla)



cnx.close()
