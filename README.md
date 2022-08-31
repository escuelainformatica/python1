# python1

## variables

* string (str)

```python
variable = "hola mundo"
```

* int (int)
```python
variable = 20
```

* float (float)
```python
variable = 20.3
```

* list (list)

> Nota: los listados son modificables, es decir, se puede agregar o quitar valores

```python
variable = [1,2,3]
```

* tuples (tuple)

> Nota: los tuples no son modificables

```python
variable = (1,2,3)
```

* diccionario (dict)

```python
producto = {"nombre":"cocacola","precio":300}
```

## transformaciones

```python
# algo en un texto
variable=str(valor2)
variable=int(valor2)
variable=bool(valor2)
variable=float(valor2)
variable=dict(valor2)
variable=tuple(valor2)
```

## f-string

```python
nombre="john"
apellido="doe"

print(nombre+apellido) # johndoe
print(nombre+' '+apellido) # john doe
print(f"{nombre} {apellido}")  # john doe


```