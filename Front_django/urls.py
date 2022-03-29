from django.urls import path

from Front_django.view import loginView, recomendacionesView, popularesView, accesoView, registroView, perfilView

urlpatterns = [
    path('', loginView),
    path('acceso/', accesoView),
    path('registro/', registroView),
    path('recomendaciones/', recomendacionesView),
    path('populares/', popularesView),
    path('perfil/', perfilView),
]
