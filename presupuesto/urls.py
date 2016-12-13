from django.conf.urls import patterns, include, url
from presupuesto.reports import reporte_presupuesto
from presupuesto.views import PresupuestoListView

urlpatterns = [
    url(r'^presupuesto/(?P<presupuesto_id>\d+)/print/$',reporte_presupuesto,name='reporte_presupuesto'),
    url(r'^presupuesto/$', PresupuestoListView.as_view(),name='presupuesto_lis'),

]