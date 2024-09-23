
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginViewSets


router = DefaultRouter()

router.register(r'login', LoginViewSets)

urlpatterns = [
    path("", include(router.urls)),
    # path('app2/', include('app2.urls'))

  

]