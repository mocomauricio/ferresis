from producto.models import *
producto = Producto.objects.get(pk=548)
producto.delete()