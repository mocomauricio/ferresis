from producto.models import *
from django.db.models import Q
productos = Producto.objects.all()
precios_venta = PrecioVentaProducto.objects.all()
precios_compra = PrecioCompraProducto.objects.all()

for i in precios_venta:
    productos = productos.exclude(id=i.producto.id)

for j in productos:
    print "ID: " + str(j.id)

quit()