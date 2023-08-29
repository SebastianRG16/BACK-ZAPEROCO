from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from consultas import views, consumers

# Configuración del enrutador para las rutas HTTP
router = routers.DefaultRouter()
router.register(r'donation', views.DonationView, 'donation')

# Configuración de las rutas WebSocket
websocket_urlpatterns = [
    path(r'ws/some_path/', consumers.DonationConsumer.as_asgi()),
]

# Rutas totales para las rutas HTTP
urlpatterns = [
    path("", include(router.urls)),
    path("docs/", include_docs_urls(title="Donacion API"))
]

# Agregar las rutas WebSocket a las rutas totales
urlpatterns += websocket_urlpatterns