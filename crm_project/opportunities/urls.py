# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import opportunitiesViewSet

# router = DefaultRouter()

# router.register(r'opportunities',opportunitiesViewSet)

# urlpatterns = [
#     path('', include(router.urls))
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import opportunitiesViewSet

router = DefaultRouter()
router.register(r'opportunities', opportunitiesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
