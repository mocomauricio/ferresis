from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
#from reportlab.lib.pagesizes import letter, LEGAL, landscape
from reportlab.lib.pagesizes import A4

from reportlab.platypus import Table
from io import BytesIO
from reportlab.lib.units import mm

from django.http.response import HttpResponse
from datetime import datetime

from presupuesto.models import Presupuesto, DetallePresupuesto

def reporte_presupuesto(request, presupuesto_id):
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "presupuesto_"+ datetime.now().strftime('%Y-%m-%d|%H:%M:%S') + '.pdf' 
    print pdf_name
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name.replace(" ","_")
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=(A4),
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    reporte = []
    styles = getSampleStyleSheet()
    header = Paragraph("Presupuesto", styles['Title'])
    reporte.append(header)

    presupuesto = Presupuesto.objects.get(pk=presupuesto_id)

    numero = Paragraph("Numero: %s" % str(presupuesto_id), styles['Normal'])
    reporte.append(numero)

    fecha = Paragraph("Fecha: %s" % presupuesto.fecha.strftime("%d/%m/%Y"), styles['Normal'])
    reporte.append(fecha)
  
    cliente = Paragraph("Cliente: %s" % presupuesto.cliente.nombre, styles['Normal'])
    reporte.append(cliente)

    total = Paragraph("Total: Gs. %s" % str(int(presupuesto.total)), styles['Normal'])
    reporte.append(total)

    detalles = DetallePresupuesto.objects.filter(presupuesto_id = presupuesto_id)
    datos = [("Producto", "Cantidad", "Precio Unitario", "Subtotal")]

    header = Paragraph("detalle", styles['Title'])
    reporte.append(header)

    for detalle in detalles:
		datos = datos + [(
							detalle.producto.nombre, 
							str(detalle.cantidad) + " " + detalle.producto.unidad_medida.abreviatura, 
							"Gs. " + str(int(detalle.precio.precio_venta - detalle.descuento)),
							"Gs. " + str(int(detalle.subtotal))
						)]

    t = Table(datos, colWidths=(100*mm,25*mm, 35*mm, 35*mm))
    t.setStyle(TableStyle(
        [
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            #('ALIGN',(3,1),(3,-1),'RIGHT'),
            #('ALIGN',(2,1),(2,-1),'RIGHT'),
            #('ALIGN',(4,1),(4,-1),'RIGHT'),
        ]
    ))
    reporte.append(t)

    doc.build(reporte)
    response.write(buff.getvalue())
    buff.close()
    return response


