from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from preregistro import views

router = routers.DefaultRouter()
router.register(r'register', views.RegistroView, 'register')

urlpatterns = [
    path("register/" , include(router.urls)),
    # path("docs/register" , include_docs_urls(title = 'Donacion API'))
]