"""chelo19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
       url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.index', name='index'),
    url(r'^detalle_carro/(?P<object_id>\d+)/$', 'app.views.detalle_carro', name='detalle_carro'),
    url(r'^automoviles/$', 'app.views.automoviles', name='automoviles'),
    url(r'^pick_up/$', 'app.views.pick_up', name='pick_up'),
    url(r'^pago/$', 'app.views.datos_tarjeta', name='datos_tarjeta'),
    url(r'^mi_perfil/$', 'app.views.miperfil', name='mi_perfil'),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^terminos_y_condiciones/$', 'app.views.terminosCondiciones', name='terminos_y_condiciones'),
    url(r'^preguntas/$', 'app.views.preguntas', name='preguntas'),
    url(r'^pago_realizado/$', 'app.views.pago_realizado', name='pago_realizado'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)