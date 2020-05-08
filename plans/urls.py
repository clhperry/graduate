from django.urls import path
from . import views

urlpatterns = [
	path('home.html', views.home, name='plans-home'),
	path('acct.html', views.acct, name='plans-acct'),
	path('ecof.html', views.ecof, name='plans-ecof'),
	path('econ.html', views.econ, name='plans-econ'),
	path('fina.html', views.fina, name='plans-fina'),
	path('gbus.html', views.gbus, name='plans-gbus'),
	path('is.html', views.bbais, name='plans-bbais'),
	path('mark.html', views.mark, name='plans-mark'),
	path('mgmt.html', views.mgmt, name='plans-mgmt'),
	path('om.html', views.om, name='plans-om'),
	path('qfin.html', views.qfin, name='plans-qfin'),
]