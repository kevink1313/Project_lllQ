from django.urls import path , include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.inicio), name='inicio'),
    path('nosotros/', login_required(views.nosotros), name='nosotros'),
    path('peliculas/', login_required(views.peliculas), name='peliculas'),
    path('peliculas/crear', login_required(views.crear), name='crear'),
    path('peliculas/editar/<int:id>', login_required(views.editar), name='editar'),
    path('peliculas/form', login_required(views.form), name='forms'),
    path('peliculas/eliminar/<int:id>', login_required(views.eliminar), name='eliminar'),
    path('accounts/', include('django.contrib.auth.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Esto es para agregar imagenes