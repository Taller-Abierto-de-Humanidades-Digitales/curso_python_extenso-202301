#Manejo de diccionarios 

libros = ["Juanita Castañeda; Desespero; 2003, poesía", "Laura Restrepo; Demasiados Héroes; 1998; Ficción Histórica",          "Mercedes Ron; La Ocasión; 2014; Novela",          "Ana Shua; Piedra y Cielo; 1987; Cuentos",          "Gabriel García Márquez; La Mala hora; 1962; Realismo mágico"]

bibliografia = {}
id_libro = 1

for libro in libros:
    autor, titulo, fecha, tipo = libro.split("; ")
    nombre_autor, apellido_autor = autor.split()
    id_str = str(id_libro).zfill(3)
    
    bibliografia[id_str] = {"tipo": tipo,
                            "autor": [{"nombre": nombre_autor, "apellido": apellido_autor}],
                            "titulo": titulo,
                            "fecha": int(fecha),
                            "editorial": "",
                            "lugar": ""}
    id_libro += 1

print("LISTADO DE LIBROS\n")

for id_libro, libro in bibliografia.items():
    print(f"Identificador: {id_libro}")
    print(f"Título: {libro['titulo']}")
    print(f"Autor: {libro['autor'][0]['nombre']} {libro['autor'][0]['apellido']}")
    print(f"Editorial: {libro['editorial']}")
    print(f"Lugar: {libro['lugar']}")
    print(f"Fecha: {libro['fecha']}\n")

#añadir elementos al dicc

libros = ["Juanita Castañeda; Desespero; 2003, poesía",          "Laura Restrepo; Demasiados Héroes; 1998; Ficción Histórica",          "Mercedes Ron; La Ocasión; 2014; Novela",          "Ana Shua; Piedra y Cielo; 1987; Cuentos",          "Gabriel García Márquez; La Mala hora; 1962; Realismo mágico"]

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

# Artículos de revista académica
# Artículos de revista académica
revistas = [{"Revista": "Nature", "Volumen": 592, "Número": 7853, "url": "https://www.nature.com/articles/592343a"},
            {"Revista": "Science", "Volumen": 371, "Número": 6536, "url": "https://www.sciencemag.org/content/371/6536"}]

id_articulo = id_libro
for articulo in revistas:
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
    id_articulo += 1

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
                print(f"URL: {libro['url']}")
           
