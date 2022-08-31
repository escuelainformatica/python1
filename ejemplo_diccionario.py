cliente = {
    "nombre": "O'hara",
    'edad': 33,
    "direccion": "sunset blv",
    "correo": "john@doe.com"
}
print(cliente)
print("-------------------------")
print( "Nombre   :" + cliente['nombre'])
print(f"Nombre   :{cliente['nombre']}")
print( "Edad     :" + str(cliente['edad']))
print(f"Edad     :{cliente['edad']}")  # f-string
print(f"Direccion: {cliente['direccion']}")
print(f"correo: {cliente['correo']}")
