

## Bibliotecas y módulos externos 
- **`settings`**: Importa configuraciones y opciones desde el archivo `settings.py`. 
- **`mysql.connector`**: Proporciona las herramientas necesarias para establecer conexión con servidores MySQL. 
- **`tkinter`**: Biblioteca estándar de Python para el desarrollo de interfaces gráficas de usuario (GUI).

## Funciones utilitarias 

### `choose_profile(id_u, conexion)`
Selecciona un perfil asociado a un usuario específico.

- **Parámetros:**
  - `id_u`: ID del usuario (tipo `int` o `str` dependiendo de la configuración de la base de datos).
  - `conexion`: Conexión activa a la base de datos MySQL.

- **Flujo:**
  1. Llama a la función `get_profiles` para recuperar la lista de perfiles asociados al usuario.
  2. Pasa la lista de perfiles a `Get_user_profile`, que solicita al usuario seleccionar un perfil.
  3. Devuelve el ID del perfil seleccionado.

- **Retorno:**
  - `profil_choosen`: ID del perfil elegido por el usuario.

### `get_profiles(id_u, conexion)`
Obtiene una lista de perfiles asociados a un usuario específico.

- **Parámetros:**
  - `id_u`: ID del usuario cuya lista de perfiles se desea recuperar.
  - `conexion`: Conexión activa a la base de datos MySQL.

- **Flujo:**
  1. Ejecuta una consulta SQL para obtener los nombres y IDs de los perfiles asociados al usuario.
  2. Utiliza un cursor para manejar la consulta y devuelve los resultados.

- **Retorno:**
  - Una lista de tuplas, donde cada tupla contiene el nombre del perfil y su ID.


### `Sections(id_profile, conexion)`
Obtiene y devuelve las películas y series no terminadas asociadas a un perfil, con nombres formateados.

- **Parámetros:**
  - `id_profile`: ID del perfil asociado al usuario.
  - `conexion`: Conexión activa a la base de datos.

- **Flujo:**
  1. Llama a `Get_videos_no_finalizados` para obtener las películas y series no terminadas.
  2. Formatea los nombres de las películas y series con el formato `[id]-nombre`.
  3. Devuelve las listas formateadas.

- **Retorno:**
  - `pelis_formateadas`: Lista de nombres de películas con formato `[id]-nombre`.
  - `series_formateadas`: Lista de nombres de series con formato `[id]-nombre`.


### `Get_videos_no_finalizados(id_profile, conexion)`
Obtiene las películas y series no terminadas asociadas a un perfil.

- **Parámetros:**
  - `id_profile`: ID del perfil asociado al usuario.
  - `conexion`: Conexión activa a la base de datos.

- **Flujo:**
  1. Consulta las películas no terminadas (`progreso < 100`).
  2. Consulta los capítulos de series no terminados (`progreso < 100`).
  3. Verifica si hay series vistas cuyo último capítulo no esté completado.
  4. Combina los resultados y devuelve las películas y series pendientes.

- **Retorno:**
  - `pelis`: Lista de IDs de películas no terminadas.
  - `caps + series_por_terminar`: Lista combinada de series con capítulos pendientes y series por terminar sin capítulos pendientes.


### `get_pelis_name(id_pelis, conexion)`
Devuelve los nombres de las películas especificadas por sus IDs.

- **Parámetros:**
  - `id_pelis`: Lista de IDs de las películas.
  - `conexion`: Conexión activa a la base de datos.

- **Flujo:**
  1. Ejecuta una consulta SQL para obtener el nombre de cada película en la lista `id_pelis`.
  2. Devuelve los nombres como una lista.

- **Retorno:**
  - Lista de nombres de las películas correspondientes.


### `get_series_name(id_series, conexion)`

Devuelve los nombres de las series especificadas por sus IDs.

- **Parámetros:**
    - `id_series`: Lista de IDs de las series.
    - `conexion`: Conexión activa a la base de datos.
- **Flujo:**
    1. Ejecuta una consulta SQL para obtener el nombre de cada serie en la lista `id_series`.
    2. Devuelve los nombres como una lista.
- **Retorno:**
    - Lista de nombres de las series correspondientes.


### `get_producciones_recientes(conexion)`
Obtiene las películas y series agregadas hace menos de 15 días.

- **Parámetros:**
  - `conexion`: Conexión activa a la base de datos.

- **Flujo:**
  1. Llama a `get_pelis_recientes` para obtener las películas recientes.
  2. Llama a `get_series_recientes` para obtener las series recientes.
  3. Devuelve los resultados como una tupla.

- **Retorno:**
  - Una tupla compuesta de:
    - `pelis`: Lista de películas recientes.
    - `series`: Lista de series recientes.


### `get_pelis_recientes(conexion)`
Obtiene hasta 5 películas que fueron agregadas hace menos de 15 días.

- **Parámetros:**
  - `conexion`: Conexión activa a la base de datos.

- **Flujo:**
  1. Ejecuta una consulta SQL para seleccionar las películas agregadas en los últimos 15 días, limitando el resultado a 5 registros.
  2. Devuelve los resultados.

- **Retorno:**
  - Lista de tuplas, donde cada tupla contiene:
    - `id_video`: ID de la película.
    - `nombre_video`: Nombre de la película.

### `get_series_recientes(conexion)`

Obtiene hasta 5 series que fueron agregadas hace menos de 15 días.

- **Parámetros:**
    
    - `conexion`: Conexión activa a la base de datos.
- **Flujo:**
    
    1. Ejecuta una consulta SQL para seleccionar las series agregadas en los últimos 15 días, limitando el resultado a 5 registros.
    2. Devuelve los resultados.
- **Retorno:**
    
    - Lista de tuplas, donde cada tupla contiene:
        - `id_serie`: ID de la serie.
        - `nombre_serie`: Nombre de la serie.


### `searchtitles(cadena, conexion, infante=0)`
Busca títulos de series o películas que contienen una cadena específica en su nombre.

- **Parámetros:**
  - `cadena`: Subcadena que se busca en los títulos.
  - `conexion`: Conexión activa a la base de datos.
  - `infante` (opcional): Si es `1`, filtra solo contenido apto para todo público (ATP).

- **Retorno:**
  - Un diccionario con la estructura:
    ```python
    {
        "m": <lista de IDs de películas>,
        "s": <lista de IDs de series>
    }
    ```


### `abouttitle(id, conexion, tipo="g", infante=0)`
Obtiene información detallada de un título según su tipo.

- **Parámetros:**
  - `id`: ID del título a buscar.
  - `conexion`: Conexión activa a la base de datos.
  - `tipo` (opcional): Especifica el tipo de contenido:
    - `"g"`: Genérico (nombre y descripción).
    - `"m"`: Película (agrega saga y descripción).
    - `"s"`: Serie (agrega cantidad de capítulos).
    - `"c"`: Capítulo (agrega temporada y serie).
  - `infante` (opcional): Si es `1`, filtra solo contenido ATP.

- **Retorno:**
  - Un diccionario con la información relevante al tipo de contenido.


### `creditos(id, conexion, tipo="g")`
Busca los créditos relacionados con un contenido (película, serie o capítulo).

- **Parámetros:**
  - `id`: ID del contenido.
  - `conexion`: Conexión activa a la base de datos.
  - `tipo` (opcional): Especifica el tipo de contenido:
    - `"g"`: Aplica a cualquier tipo de contenido
    - `"m"`: Aplica solo a películas.
    - `"c"`: Aplica solo a capítulos.
    - `"s"`: Aplica solo a series.

- **Retorno:**
  - Un diccionario con las claves `"Actores"`, `"Directores"`, y `"Productores"`. Cada clave contiene una lista de tuplas con la información del artista:
    - Actores: `(nombre, apellido, pseudónimo, personaje)`
    - Directores y Productores: `(nombre, apellido, pseudónimo)`


