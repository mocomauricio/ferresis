import json
from django.http import HttpResponse
from producto.models import *
from extra.globals import separador_de_miles


def get_precioventa(request):
    precioventa_id = (request.GET['precioventa_id']).replace(" ","")
    print "ajax precioventa_id (%s)" % precioventa_id

    result_set = []

    if precioventa_id == "":
        return HttpResponse(json.dumps(result_set), 
                            #mimetype='application/json', 
                            content_type='application/json')

    precioventa_id = int(precioventa_id)

    precioventa = PrecioVentaProducto.objects.get(pk = precioventa_id)

    result_set.append({ 'precio': separador_de_miles(precioventa.precio_venta) })

    return HttpResponse(json.dumps(result_set), 
                        content_type='application/json')


def get_listapreciosventa(request):
    producto_id = (request.GET['producto_id']).replace(" ","")
    print "ajax producto_id (%s)" % producto_id

    result_set = []

    if producto_id == "":
        return HttpResponse(json.dumps(result_set), 
                            content_type='application/json')

    producto_id = int(producto_id)

    precios = PrecioVentaProducto.objects.filter(producto_id = producto_id)

    for precio in precios:
        result_set.append({'id': precio.id, 'precio': precio.__unicode__()})

    return HttpResponse(json.dumps(result_set), 
                        content_type='application/json')


    
def get_preciocompra(request):
    preciocompra_id = (request.GET['preciocompra_id']).replace(" ","")
    print "ajax preciocompra_id (%s)" % preciocompra_id

    result_set = []

    if preciocompra_id == "":
        return HttpResponse(json.dumps(result_set), 
                            #mimetype='application/json', 
                            content_type='application/json')

    preciocompra_id = int(preciocompra_id)

    preciocompra = PrecioCompraProducto.objects.get(pk = preciocompra_id)

    result_set.append({ 'precio': separador_de_miles(preciocompra.precio_compra) })

    return HttpResponse(json.dumps(result_set), 
                        content_type='application/json')


def get_listaprecioscompra(request):
    producto_id = (request.GET['producto_id']).replace(" ","")
    print "ajax producto_id (%s)" % producto_id

    result_set = []

    if producto_id == "":
        return HttpResponse(json.dumps(result_set), 
                            content_type='application/json')

    producto_id = int(producto_id)

    precios = PrecioCompraProducto.objects.filter(producto_id = producto_id)

    for precio in precios:
        result_set.append({'id': precio.id, 'precio': precio.__unicode__()})

    return HttpResponse(json.dumps(result_set), 
                        content_type='application/json')