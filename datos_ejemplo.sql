INSERT INTO Usuarios (e_mail, password) VALUES
('juanperez@gmail.com', 'juansuper123'),
('marianoro@gmail.com', 'mariano1234'),
('aledromar@yahoo.com', 'alejandro123'),
('carlaruiz@hotmail.com', 'carla_2023'),
('lucasgarc@gmail.com', 'lucaspass567'),
('sofialopez@yahoo.com', 'sofia1234'),
('gabisanchez@gmail.com', 'gaby5678'),
('mariarosario@gmail.com', 'mariarosa123'),
('rodrimartinez@live.com', 'rodrigo987'),
('viviperez@gmail.com', 'vivi1234'),
('marcesanchez@mail.com', 'marcelo1111'),
('naty@hotmail.com', 'natalia987'),
('lilifer@outlook.com', 'lili2024'),
('carlos@gmail.com', 'carlospass2023'),
('vero@yahoo.com', 'veronica9987');



INSERT INTO Autenticaciones (id_usuario, success, momento) VALUES
(1, true, '2024-11-01 08:15:00'),
(2, false, '2024-11-01 09:25:00'),
(3, true, '2024-11-02 10:35:00'),
(4, true, '2024-11-03 11:45:00'),
(5, false, '2024-11-04 12:55:00'),
(6, true, '2024-11-05 13:05:00'),
(7, true, '2024-11-06 14:15:00'),
(8, true, '2024-11-07 15:25:00'),
(9, false, '2024-11-08 16:35:00'),
(10, true, '2024-11-09 17:45:00'),
(11, true, '2024-11-10 18:55:00'),
(12, false, '2024-11-11 19:05:00'),
(13, true, '2024-11-12 20:15:00'),
(14, true, '2024-11-13 21:25:00'),
(15, false, '2024-11-14 22:35:00'),
(1, true, '2024-11-15 08:45:00'),
(2, true, '2024-11-16 09:55:00'),
(3, true, '2024-11-17 10:05:00'),
(4, false, '2024-11-18 11:15:00'),
(5, true, '2024-11-19 12:25:00'),
(6, false, '2024-11-20 13:35:00'),
(7, true, '2024-11-21 14:45:00'),
(8, true, '2024-11-22 15:55:00'),
(9, false, '2024-11-23 16:05:00'),
(10, true, '2024-11-24 17:15:00'),
(11, true, '2024-11-25 18:25:00'),
(12, false, '2024-11-26 19:35:00'),
(13, true, '2024-11-27 20:45:00'),
(14, false, '2024-11-28 21:55:00'),
(15, true, '2024-11-29 22:05:00');



INSERT INTO Perfiles (id_usuario, nombre_perfil, es_infante) VALUES
(1, 'Juanito', false),
(1, 'Juancito', true),
(2, 'MarianoFan', false),
(2, 'Mari12', true),
(3, 'Alejo', false),
(3, 'Alejito', true),
(4, 'Carla2023', false),
(4, 'CarlaRosa', true),
(5, 'Lucas_M', false),
(5, 'Luciano', true),
(6, 'Sofi_Lopez', false),
(6, 'Sofia_Suarez', true),
(7, 'Gaby24', false),
(7, 'Gabriela', true),
(8, 'Marita', false),
(8, 'Mari_Rosa', true),
(9, 'Rodri', false),
(9, 'Rodrigo69', true),
(10, 'Vivi', false),
(10, 'Viviana2024', true),
(11, 'MarceloS', false),
(11, 'MarceloG', true),
(12, 'NataliaF', false),
(12, 'Nati', true),
(13, 'Liliana_Fern', false),
(13, 'Lili_Fernandez', true),
(14, 'CarlosG', false),
(14, 'CarlosGarcia', true),
(15, 'VeronicaJ', false),
(15, 'VeroJ', true);




INSERT INTO Artistas (nombre_artista, apellido_artista, pseudonimo_artista) VALUES
('Leonardo', 'DiCaprio', 'Leo'),
('Scarlett', 'Johansson', 'Scarlett'),
('Robert', 'Downey', 'RDJ'),
('Chris', 'Hemsworth', 'Thor'),
('Tom', 'Hiddleston', 'Loki'),
('Emma', 'Watson', 'Hermione'),
('Johnny', 'Depp', 'Jack Sparrow'),
('Angelina', 'Jolie', 'Angie'),
('Brad', 'Pitt', 'Bradster'),
('Meryl', 'Streep', 'Meryl'),
('Tom', 'Cruise', 'Tommy'),
('Will', 'Smith', 'Big Willy'),
('Charlize', 'Theron', 'Charlize'),
('Matthew', 'McConaughey', 'Matty'),
('Dwayne', 'Johnson', 'The Rock'),
('Julia', 'Roberts', 'Julia'),
('Gary', 'Oldman', 'Gary'),
('Al', 'Pacino', 'Al'),
('Morgan', 'Freeman', 'Morgan'),
('Cate', 'Blanchett', 'Cate'),
('Jessica', 'Chastain', 'Jessica'),
('Tom', 'Hardy', 'Tommy H'),
('Idris', 'Elba', 'Idris'),
('Chris', 'Evans', 'Capitan'),
('Jennifer', 'Lawrence', 'JLaw'),
('Samuel', 'Jackson', 'Sam'),
('Vin', 'Diesel', 'Vin'),
('Keanu', 'Reeves', 'Neo'),
('Nicole', 'Kidman', 'Nicole'),
('Nicole', 'Kidman', 'Nicole Kid');




INSERT INTO Videos (ubicacion, nombre_video, descripcion_video, atp) VALUES
('/videos/ironman.mp4', 'Iron Man - 2008', 'Tony Stark se convierte en Iron Man.',True),
('/videos/blackwidow.mp4', 'Black Widow - 2021', 'Natasha Romanoff enfrenta su pasado.',True),
('/videos/spiderman.mp4', 'Spider-Man: Homecoming - 2017', 'Peter Parker se adapta a su nueva vida.',True),
('/videos/captainamerica.mp4', 'Captain America - 2011', 'Steve Rogers lucha por la libertad.',True),
('/videos/thor.mp4', 'Thor - 2011', 'Thor, el dios del trueno, llega a la Tierra.',True),
('/videos/avengers.mp4', 'Avengers - 2012', 'Los Vengadores se unen para salvar el mundo.',True),
('/videos/blackpanther.mp4', 'Black Panther - 2018', 'T\'Challa lucha por el trono de Wakanda.',True),
('/videos/antman.mp4', 'Ant-Man - 2015', 'Scott Lang debe proteger el traje de Ant-Man.',False),
('/videos/endgame.mp4', 'Avengers: Endgame - 2019', 'El enfrentamiento final contra Thanos.',True),
('/videos/strangerthings.mp4', 'Stranger Things - 2016', 'Una serie que explora lo sobrenatural en Hawkins, Indiana.',False),
('/videos/got.mp4', 'Game of Thrones - 2011', 'La lucha por el trono de hierro comienza.',False),
('/videos/wandavision.mp4', 'WandaVision - 2021', 'Wanda y Vision descubren la realidad que los rodea.',True),
('/videos/loki.mp4', 'Loki - 2021', 'Loki explora el multiverso tras el fin de Endgame.',True),
('/videos/daredevil.mp4', 'Daredevil - 2015', 'Matt Murdock lucha por la justicia.',False),
('/videos/jessicajones.mp4', 'Jessica Jones - 2015', 'Jessica enfrenta un peligro mortal en Nueva York.',True);





INSERT INTO Sagas (nombre_saga, descripcion_saga) VALUES
('Avengers', 'Saga de los Vengadores que enfrenta a héroes contra grandes amenazas.'),
('Spider-Man', 'Saga centrada en Spider-Man y sus aventuras.'),
('Thor', 'Las aventuras del dios del trueno Thor.'),
('X-Men', 'Una saga sobre los mutantes que luchan por la aceptación en el mundo.'),
('Star Wars', 'La lucha épica entre la rebelión y el imperio en una galaxia lejana.');




INSERT INTO Peliculas (id_video, id_saga) VALUES
(1, 1), -- Avengers
(2, 1), -- Avengers Endgame
(3, 1), -- Avengers Infinity War
(4, 2), -- Spider-Man: Homecoming
(5, 2), -- Spider-Man: No Way Home
(6, 3), -- Thor: Ragnarok
(7, 3), -- Thor: Love and Thunder
(8, 4), -- X-Men: Days of Future Past
(9, 5), -- Star Wars: A New Hope
(10, 5), -- Star Wars: The Empire Strikes Back
(11, 5), -- Star Wars: Return of the Jedi
(12, 1), -- Avengers: Civil War
(13, 2), -- Avengers: Age of Ultron
(14, 3), -- Thor: The Dark World;
(15, 4); -- X-Men: Apocalypse



INSERT INTO Progresos (id_perfil, id_video, tiempo_progreso) VALUES
(1, 1, '01:00:00'),
(2, 2, '00:30:00'),
(3, 3, '02:30:00'),
(4, 4, '01:45:00'),
(5, 5, '00:20:00'),
(6, 6, '01:10:00'),
(7, 7, '00:50:00'),
(8, 8, '00:35:00'),
(9, 9, '01:00:00'),
(10, 10, '02:15:00'),
(11, 11, '01:00:00'),
(12, 12, '01:30:00'),
(13, 13, '02:45:00'),
(14, 14, '00:10:00'),
(15, 15, '02:00:00'),
(1, 6, '01:30:00'),
(2, 7, '00:20:00'),
(3, 8, '01:00:00');



INSERT INTO Creditos (id_artista, id_video, rol, nombre_personaje) VALUES
(1, 1, 'Actor', 'Tony Stark'),
(2, 1, 'Actor', 'Natasha Romanoff'),
(3, 1, 'Director', 'Joss Whedon'),
(4, 1, 'Productor', 'Kevin Feige'),
(5, 4, 'Actor', 'Peter Parker'),
(6, 4, 'Director', 'Jon Watts'),
(7, 4, 'Productor', 'Kevin Feige'),
(8, 9, 'Actor', 'Luke Skywalker');
