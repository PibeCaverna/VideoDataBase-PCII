CREATE TABLE Usuarios(
	id_usuario INT PRIMARY KEY AUTO_INCREMENT,
	e_mail VARCHAR(20) UNIQUE NOT NULL,
	password VARCHAR(20) NOT NULL
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
	nombre_perfil VARCHAR(20),
	es_infante BOOLEAN NOT NULL,
	
	FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
)
#
CREATE TABLE Artistas(
	id_artista INT PRIMARY KEY AUTO_INCREMENT,
	nombre_artista VARCHAR(20) NOT NULL,
	apellido_artista VARCHAR(20) NOT NULL,
	pseudonimo_artista VARCHAR(20)
)
#
CREATE TABLE Videos(
	id_video INT PRIMARY KEY AUTO_INCREMENT,
	ubicacion VARCHAR(100),
	nombre_video VARCHAR(20) NOT NULL,
	descripcion_video VARCHAR(200)
)
#
CREATE TABLE Series(
	id_serie INT PRIMARY KEY AUTO_INCREMENT,
	nombre_serie VARCHAR(20) NOT NULL,
	descripcion_serie VARCHAR(200)
)
#
CREATE TABLE Capitulos(
	id_capitulo INT PRIMARY KEY,
	id_serie INT NOT NULL,
	temporada INT,

	FOREIGN KEY (id_capitulo) REFERENCES Videos(id_video),
	FOREIGN KEY (id_serie) REFERENCES Series(id_serie)
)
#
CREATE TABLE Sagas(
	id_saga INT PRIMARY KEY AUTO_INCREMENT,
	nombre_saga VARCHAR(20) NOT NULL,
	descripcion_saga VARCHAR(200)
)
#
CREATE TABLE Peliculas(
	id_pelicula INT PRIMARY KEY,
	id_saga INT,

	FOREIGN KEY (id_pelicula) REFERENCES Videos(id_video),
	FOREIGN KEY (id_saga) REFERENCES Sagas(id_saga)
)
#
CREATE TABLE Progresos(
	id_perfil INT,
	id_video INT,
	tiempo_progreso TIME,

	PRIMARY KEY (id_perfil, id_video),
	FOREIGN KEY (id_perfil) REFERENCES Perfiles(id_perfil),
	FOREIGN KEY (id_video) REFERENCES Videos(id_video)
)
#
CREATE TABLE Creditos(
	id_artista INT NOT NULL,
	id_video INT NOT NULL,
	rol SET("Actor","Director","Productor"),
	nombre_personaje VARCHAR(20),
	
	PRIMARY KEY (id_artista, id_video),
	FOREIGN KEY (id_artista) REFERENCES Artistas(id_artista),
	FOREIGN KEY (id_video) REFERENCES Videos(id_video)
)