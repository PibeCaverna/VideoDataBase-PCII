CREATE TABLE Usuarios(
	id_usuario INT PRIMARY KEY AUTO_INCREMENT,
	e_mail VARCHAR(20) NOT NULL,
	password VARCHAR(20) NOT NULL
)
#
CREATE TABLE Autenticaciones(
	id_auth INT PRIMARY KEY AUTO_INCREMENT,
	id_usuario INT,
	success BOOLEAN NOT NULL,
	momento TIMESTAMP, 
	
	FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
)
#
CREATE TABLE Perfiles(
	id_peril INT PRIMARY KEY AUTO_INCREMENT,
	id_usuario INT,
	es_infante BOOLEAN NOT NULL,
	
	FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
)
#
CREATE TABLE Artistas(
	id_artista INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(20),
	apellido VARCHAR(20),
	pseudonimo VARCHAR(20)
)
