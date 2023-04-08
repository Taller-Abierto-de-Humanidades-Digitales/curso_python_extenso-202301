#Manejo de diccionarios 

libros = ["Juanita Castañeda; Desespero; 2003; poesía", "Laura Restrepo; Demasiados Héroes; 1998; Ficción Histórica", "Mercedes Ron; La Ocasión; 2014; Novela", "Ana Shua; Piedra y Cielo; 1987; Cuentos", "Gabriel García Márquez; La Mala hora; 1962; Realismo mágico"]

bibliografia = {}
id_libro = 1

for libro in libros:
    autor, titulo, fecha, tipo = libro.split("; ")
    # nombre_autor, apellido_autor = autor.split() # Esto no funciona si el autor tiene más de un apellido
    # Una opción es usar la función split() dos veces
    if len(autor.split()) == 2:
        nombre_autor, apellido_autor = autor.split()
    elif len(autor.split()) == 3:
        nombre_autor, apellido1, apellido2 = autor.split()
        apellido_autor = f"{apellido1} {apellido2}"

    id_str = str(id_libro).zfill(3)
    bibliografia[id_str] = {"tipo": tipo,
                            "autor": [{"nombre": nombre_autor, "apellido": apellido_autor}],
                            "titulo": titulo,
                            "fecha": int(fecha),
                            "editorial": "",
                            "lugar": ""}
    id_libro += 1

##  TODO: Deberás actualizar el diccionario con la información que no haya estado disponible en tu listado original. Por ejemplo:

editoriales = {"001": "Editorial Planeta", "002": "Editorial Planeta", "003": "Editorial Planeta", "004": "Editorial Planeta", "005": "Editorial Planeta"}
lugares = {"001": "Bogotá", "002": "Bogotá", "003": "Bogotá", "004": "Bogotá", "005": "Bogotá"}

print("LISTADO DE LIBROS\n")

for id_libro, libro in bibliografia.items():
    print(f"Identificador: {id_libro}")
    print(f"Título: {libro['titulo']}")
    print(f"Autor: {libro['autor'][0]['nombre']} {libro['autor'][0]['apellido']}")
    print(f"Editorial: {libro['editorial']}")
    print(f"Lugar: {libro['lugar']}")
    print(f"Fecha: {libro['fecha']}\n")

#añadir elementos al dicc
""" Como el diccionario ya se creó, no es necesario volver a hacerlo.

libros = ["Juanita Castañeda; Desespero; 2003, poesía", "Laura Restrepo; Demasiados Héroes; 1998; Ficción Histórica", "Mercedes Ron; La Ocasión; 2014; Novela", "Ana Shua; Piedra y Cielo; 1987; Cuentos", "Gabriel García Márquez; La Mala hora; 1962; Realismo mágico"]

bibliografia = {}

id_libro = 1
for libro in libros:
    campos = libro.split("; ")
    autor = campos[0].split()
    nombre_autor = autor[0]
    apellido_autor = " ".join(autor[1:])
    titulo = campos[1]
    fecha = int(campos[2])
    tipo = campos[3]

    libro_dict = {"tipo": tipo,
                  "autor": [{"nombre": nombre_autor, "apellido": apellido_autor}],
                  "titulo": titulo,
                  "fecha": fecha,
                  "editorial": "",
                  "lugar": ""}

    bibliografia[id_libro] = libro_dict
    id_libro += 1
 """
# Artículos de revista académica
# Artículos de revista académica

# En este caso, hacen falta los campos básicos de la bibliografía: autor, título y fecha.
# POr ejemplo: {"tipo": "Artículo de revista", "autor": [{"nombre": "Juan", "apellido": "Pérez"}], "titulo": "Título del artículo", "fecha": 2020, "revista": "Nature", "volumen": 592, "numero": 7853, "url": "https://www.nature.com/articles/592343a}
revistas = [{"Revista": "Nature", "Volumen": 592, "Número": 7853, "url": "https://www.nature.com/articles/592343a"},
            {"Revista": "Science", "Volumen": 371, "Número": 6536, "url": "https://www.sciencemag.org/content/371/6536"}]

# id_articulo = id_libro # Aunque puede funcionar, esto no es buena práctica. Si en el futuro se agregan más libros, el id de los artículos se verá afectado.
for articulo in revistas:
    # obtener el último id de bibliografía y sumarle 1
    id_articulo = int(max(bibliografia.keys())) + 1
    id_articulo = str(id_articulo).zfill(3)
    revista = articulo["Revista"]
    volumen = articulo["Volumen"]
    numero = articulo["Número"]
    url = articulo["url"]

    articulo_dict = {"tipo": "Artículo de revista",
                     "autor": [{"nombre": "", "apellido": ""}],
                     "titulo": "",
                     "fecha": 0,
                     "editorial": revista,
                     "lugar": "",
                     "volumen": volumen,
                     "numero": numero,
                     "url": url}

    bibliografia[id_articulo] = articulo_dict
    # id_articulo += 1 # No es necesario porque se está usando el id de bibliografía

""" Esta función es útil, pero haremos uso de esta funcionalidad en el siguiente ejercicio.
def mostrar_por_tipo(tipo):
    print(f"LISTADO DE {tipo.upper()}\n")
    for id_libro, libro in bibliografia.items():
        if libro["tipo"] == tipo:
            print(f"Identificador: {id_libro}")
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor'][0]['nombre']} {libro['autor'][0]['apellido']}")
            print(f"Editorial: {libro['editorial']}")
            print(f"Lugar: {libro['lugar']}")
            print(f"Fecha: {libro['fecha']}")
            if tipo == "Artículo de revista":
                print(f"Volumen: {libro['volumen']}")
                print(f"Número: {libro['numero']}")
                print(f"URL: {libro['url']}") """
           
# TODO: Debes repetir el proceso con artículos de periódico y con videos de YouTube.
# Además, realizar los ejercicios 3 y 4

