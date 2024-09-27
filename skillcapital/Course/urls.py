from django.urls import path,include
from .views import Courseviewset
from rest_framework.routers import DefaultRouter

Router=DefaultRouter()

Router.register(r"Course",Courseviewset)

urlpatterns=[
    path("",include(Router.urls))
]