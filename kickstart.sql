CREATE TABLE Usuarios(
	id_usuario INT PRIMARY KEY AUTO_INCREMENT,
	e_mail varchar(255) UNIQUE NOT NULL,
	password varchar(255) NOT NULL
)
#
CREATE TABLE Autenticaciones(
	id_auth INT PRIMARY KEY AUTO_INCREMENT,
	id_usuario INT NOT NULL,
	success BOOLEAN NOT NULL,
	momento TIMESTAMP NOT NULL, 
	
	FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
)
#
CREATE TABLE Perfiles(
	id_perfil INT PRIMARY KEY AUTO_INCREMENT,
	id_usuario INT NOT NULL,
	nombre_perfil VARCHAR(31),
	es_infante BOOLEAN NOT NULL,
	
	FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
)
#
CREATE TABLE Artistas(
	id_artista INT PRIMARY KEY AUTO_INCREMENT,
	nombre_artista varchar(50) NOT NULL,
	apellido_artista varchar(50) NOT NULL,
	pseudonimo_artista varchar(50)
)
#
CREATE TABLE Videos(
	id_video INT PRIMARY KEY AUTO_INCREMENT,
	ubicacion varchar(255),
	nombre_video varchar(255) NOT NULL,
	descripcion_video varchar(2047),
	atp BOOLEAN NOT NULL
)
#
CREATE TABLE Series(
	id_serie INT PRIMARY KEY AUTO_INCREMENT,
	nombre_serie varchar(255) NOT NULL,
	descripcion_serie varchar(2047),
	atp BOOLEAN NOT NULL,
	fecha_agreg_serie DATE NOT NULL
)
#
CREATE TABLE Capitulos(
	id_video INT PRIMARY KEY,
	id_serie INT NOT NULL,
  	num_capitulo INT NOT NULL,
	temporada INT,

	FOREIGN KEY (id_video) REFERENCES Videos(id_video),
	FOREIGN KEY (id_serie) REFERENCES Series(id_serie)
)
#
CREATE TABLE Sagas(
	id_saga INT PRIMARY KEY AUTO_INCREMENT,
	nombre_saga varchar(255) NOT NULL,
	descripcion_saga varchar(2047)
)
#
CREATE TABLE Peliculas(
	id_video INT PRIMARY KEY,
	id_saga INT,
	fecha_agreg_peli DATE NOT NULL,

	FOREIGN KEY (id_video) REFERENCES Videos(id_video),
	FOREIGN KEY (id_saga) REFERENCES Sagas(id_saga)
)
#
CREATE TABLE Progresos(
	id_perfil INT,
	id_video INT,
	progreso INT,

	PRIMARY KEY (id_perfil, id_video),
	FOREIGN KEY (id_perfil) REFERENCES Perfiles(id_perfil),
	FOREIGN KEY (id_video) REFERENCES Videos(id_video)
)
#
CREATE TABLE Creditos(
	id_artista INT NOT NULL,
	id_video INT NOT NULL,
	rol SET("Actor","Director","Productor"),
	nombre_personaje VARCHAR(255),
	
	PRIMARY KEY (id_artista, id_video),
	FOREIGN KEY (id_artista) REFERENCES Artistas(id_artista),
	FOREIGN KEY (id_video) REFERENCES Videos(id_video)
)
