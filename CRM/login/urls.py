from django.urls import path
# from rest_framework.routers import DefaultRouter
from .views import Register,login

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', login.as_view()),
]
# router = DefaultRouter()
# router.register(r'users', SomeOtherViewSet)
# # router.register(r"register",login)
# # router.register(r"login",login)
# urlpatterns=[
#     path("",include(router.urls))
# ]
