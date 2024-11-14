CREATE DATABASE dilfar_VideoDB-PCII;

USE dilfar_VideoDB-PCII;

CREATE TABLE Usuarios(
	id_usuario INT PRIMARY KEY AUTO_INCREMENT,
	e_mail VARCHAR(20) NOT NULL,
	password VARCHAR(20) NOT NULL
)

CREATE TABLE Autenticaciones(
	id_auth INT PRIMARY KEY AUTO_INCREMENT,
	id_usuario INT FOREIGN KEY REFERENCES Usuarios(id_usuario),
	success BOOLEAN NOT NULL,
	momento TIMESTAMP, #preguntar la diferencia entre DATETIME y TIMESTAMP
)

CREATE TABLE Perfiles(
	id_perfil INT PRIMARY KEY AUTO_INCREMENT,
	id_usuario INT FOREIGN KEY REFERENCES Usuarios(id_usuario),
	es_infante BOOLEAN NOT NULL
)

CREATE TABLE Artistas(
	id_artista INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(20),
	apellido VARCHAR(20),
	pseudonimo VARCHAR(20)
)
