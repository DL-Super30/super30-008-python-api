from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import login

router = DefaultRouter()

router.register(r"login",login)
urlpatterns=[
    path("",include(router.urls))
]
