# Decorador de clase para aplicar un decorador a todos los métodos de la clase
def class_decorator(decorator):
    # Función interna que recibirá la clase a la que se aplicará el decorador
    def decorator_class(cls):
        # Iterar sobre todos los atributos de la clase
        for attr_name in dir(cls):
            # Obtener el atributo de la clase usando su nombre
            attr = getattr(cls, attr_name)
            # Verificar si el atributo es callable (un método) y no es un método especial
            if callable(attr) and not attr_name.startswith("__"):
                # Aplicar el decorador al método
                decorated_attr = decorator(attr)
                # Reemplazar el método original con el decorado en la clase
                setattr(cls, attr_name, decorated_attr)
        # Retornar la clase modificada
        return cls

    # Retornar la función que aplica el decorador a la clase
    return decorator_class
